from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil
from typing import List, Optional

from parser import PDFParser
from section_detector import SectionDetector
from rag.embeddings import get_embeddings
from rag.vector_store import VectorStoreManager
from agents.explainer_agent import ExplainerAgent
from agents.simplifier_agent import SimplifierAgent
from agents.critic_agent import CriticAgent
from agents.citation_agent import CitationAgent

app = FastAPI(title="Research Paper Explainer + Critic API")

# Initialize shared components
UPLOAD_DIR = "uploads"
VECTOR_DB_DIR = "vector_db"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(VECTOR_DB_DIR, exist_ok=True)

embeddings = get_embeddings()
vsm = VectorStoreManager(embeddings)
detector = SectionDetector()

# Initialize Agents
explainer = ExplainerAgent()
simplifier = SimplifierAgent()
critic = CriticAgent()
citation_agent = CitationAgent()

@app.post("/upload")
async def upload_paper(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # 1. Parse PDF
        parser = PDFParser(file_path)
        analysis = parser.get_full_analysis()
        
        # 2. Detect Sections
        sections = detector.detect_sections(analysis["pages"])
        
        # 3. Create Vector Store
        vsm.create_vector_store(sections)
        vsm.save_vector_store(os.path.join(VECTOR_DB_DIR, file.filename))
        
        return {
            "message": "Paper uploaded and processed successfully.",
            "filename": file.filename,
            "sections": [s["section_name"] for s in sections]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask")
async def ask_question(filename: str, question: str, agent_type: str = "explainer"):
    try:
        # Load vector store for this file
        vsm.load_vector_store(os.path.join(VECTOR_DB_DIR, filename))
        
        # Retrieve context
        docs = vsm.search(question, k=5)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Select Agent
        if agent_type == "explainer":
            answer = explainer.run(context, question)
        elif agent_type == "simplifier":
            answer = simplifier.run(context, question)
        elif agent_type == "critic":
            answer = critic.run(context, question)
        elif agent_type == "citation":
            answer = citation_agent.run(context, question)
        else:
            answer = explainer.run(context, question)
            
        return {
            "answer": answer,
            "sources": [{"content": d.page_content, "metadata": d.metadata} for d in docs]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
