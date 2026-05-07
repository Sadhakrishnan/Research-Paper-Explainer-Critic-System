from .base import get_llm, create_agent_chain
import json

CITATION_PROMPT = """
You are a Citation Agent. Your goal is to extract and track references and citation usage within a research paper.

Context from the paper:
{context}

Tasks:
{question}

Instructions:
1. Extract references mentioned in the context.
2. Identify which sections use which citations.
3. If possible, provide the title and authors of the cited work.
4. Output the results in a structured format (JSON if requested, or a clear list).

Citations Analysis:
"""

class CitationAgent:
    def __init__(self):
        self.llm = get_llm()
        self.chain = create_agent_chain(self.llm, CITATION_PROMPT)

    def run(self, context: str, question: str = "Extract and analyze citations in this section."):
        return self.chain.invoke({"context": context, "question": question})
