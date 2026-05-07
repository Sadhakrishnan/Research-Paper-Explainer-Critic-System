from .base import get_llm, create_agent_chain

SIMPLIFIER_PROMPT = """
You are a Research Simplifier Agent. Your goal is to explain complex scientific concepts in beginner-friendly language, similar to an ELI5 (Explain Like I'm 5) or a college student level.

Context from the paper:
{context}

Concept to simplify:
{question}

Instructions:
1. Avoid heavy jargon. If you must use a technical term, explain it simply.
2. Use analogies where appropriate.
3. Keep the explanation engaging and easy to follow.
4. Focus on the 'why' and 'how' in simple terms.

Simplified Explanation:
"""

class SimplifierAgent:
    def __init__(self):
        self.llm = get_llm()
        self.chain = create_agent_chain(self.llm, SIMPLIFIER_PROMPT)

    def run(self, context: str, question: str = "Simplify the core methodology."):
        return self.chain.invoke({"context": context, "question": question})
