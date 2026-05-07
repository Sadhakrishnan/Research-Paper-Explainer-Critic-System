from .base import get_llm, create_agent_chain

EXPLAINER_PROMPT = """
You are a Research Paper Explainer Agent. Your goal is to provide a clear, accurate, and professional explanation of a research paper based on the provided context.

Context from the paper:
{context}

Question:
{question}

Instructions:
1. Summarize the core idea of the paper.
2. Explain the methodology used.
3. Highlight the key findings.
4. Maintain a professional and academic tone.
5. If the information is not in the context, state that you don't know.

Explanation:
"""

class ExplainerAgent:
    def __init__(self):
        self.llm = get_llm()
        self.chain = create_agent_chain(self.llm, EXPLAINER_PROMPT)

    def run(self, context: str, question: str = "Explain this paper."):
        return self.chain.invoke({"context": context, "question": question})
