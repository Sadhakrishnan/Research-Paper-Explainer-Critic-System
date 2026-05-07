from .base import get_llm, create_agent_chain

CRITIC_PROMPT = """
You are a Methodology Critic Agent. Your goal is to critically evaluate the research paper's methodology, assumptions, and results.

Context from the paper:
{context}

Specific area to critique (optional):
{question}

Instructions:
1. Identify any weak assumptions.
2. Evaluate the dataset size and diversity.
3. Check for missing baselines or comparisons.
4. Assess the evaluation metrics used.
5. Point out potential overfitting or generalization issues.
6. Be objective and constructive in your critique.

Critique:
"""

class CriticAgent:
    def __init__(self):
        self.llm = get_llm()
        self.chain = create_agent_chain(self.llm, CRITIC_PROMPT)

    def run(self, context: str, question: str = "Critique the methodology and evaluation."):
        return self.chain.invoke({"context": context, "question": question})
