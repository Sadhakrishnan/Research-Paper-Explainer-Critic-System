# Research Paper Explainer + Critic System

An AI-powered multi-agent research assistant that explains, critiques, and analyzes scientific papers using RAG, LLM reasoning, and citation-aware retrieval.

---

## 🚀 Features

- Research paper understanding and analysis
- Section-aware PDF parsing
- Multi-agent reasoning pipeline
- RAG-based question answering
- Contribution extraction
- Methodology critique generation
- Citation tracking and analysis
- Beginner-friendly paper explanations
- Structured report generation

---

## 🎯 Project Goal

The system can:

✅ Understand research paper structure  
✅ Explain concepts in simple language  
✅ Extract key contributions  
✅ Critique methodology and limitations  
✅ Track citations and references  
✅ Generate structured AI reports  

### Example Output

> “The paper proposes a privacy-preserving face recognition approach using adversarial embeddings, but evaluation on only one dataset may limit generalization.”

---

## 🧠 Core Differentiator

Most systems:
- ❌ Only summarize papers

This system:
- ✅ Explains concepts
- ✅ Critiques methodology
- ✅ Evaluates limitations
- ✅ Uses multi-agent reasoning
- ✅ Supports citation-aware retrieval

---

## ⚙️ System Architecture

```text
User Upload (PDF)
        ↓
PDF Parsing + Section Detection
        ↓
Document Chunking
        ↓
Embedding + Vector DB (RAG)
        ↓
Agent Orchestrator
   ├── Explainer Agent
   ├── Simplifier Agent
   ├── Critic Agent
   ├── Contribution Extractor
   ├── Citation Agent
        ↓
LLM Reasoning + Reflection
        ↓
Final Structured Report
```

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI

### PDF Processing
- PyMuPDF
- pdfplumber
- GROBID

### RAG Pipeline
- LangChain
- FAISS / ChromaDB
- Sentence Transformers

### Multi-Agent Framework
- CrewAI / LangGraph

### LLMs
- OpenAI API / Local LLMs

### Frontend
- Streamlit / React

---

## 📂 Core Components

### 📘 Explainer Agent
Explains paper concepts in simple language.

### 🧒 Simplifier Agent
Generates beginner-friendly explanations.

### 🧪 Contribution Extractor
Identifies novel ideas and research contributions.

### 🔍 Critic Agent
Evaluates:
- Weak assumptions
- Small datasets
- Missing baselines
- Evaluation limitations

### 📚 Citation Agent
Tracks references and citation usage.

---

## 🔁 Reflection Loop

The system uses iterative reasoning:

```text
Draft Explanation
      ↓
Critic Reviews Output
      ↓
Refined Explanation
```

This improves:
- Accuracy
- Reasoning quality
- Hallucination reduction

---

## 💬 RAG-Based Question Answering

Users can ask questions like:

- “What dataset was used?”
- “What are the limitations?”
- “What is the main contribution?”

The system retrieves relevant paper chunks and generates citation-aware answers.

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/research-paper-agent.git

cd research-paper-agent

pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Backend
```bash
uvicorn api.main:app --reload
```

### Frontend
```bash
streamlit run frontend/app.py
```

---

## 🔥 Advanced Features

- Research gap detection
- Citation network visualization
- Multi-paper comparison
- Knowledge graph generation
- Automatic literature review generation
- Research recommendation system

---

## 📊 Metrics

- Retrieval Accuracy
- Citation Precision
- Hallucination Rate
- Answer Faithfulness

---

## 🎯 Final Product Vision

An AI Research Assistant capable of understanding, evaluating, and explaining scientific literature beyond simple PDF chatbots.

---


## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
