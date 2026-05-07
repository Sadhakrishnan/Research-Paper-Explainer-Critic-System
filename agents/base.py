from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm(model_name="gpt-4o", temperature=0):
    """
    Returns the LLM instance.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        # Fallback to a mock or raise error
        # For now, we'll assume the user will provide it.
        pass
    
    return ChatOpenAI(
        model=model_name,
        temperature=temperature,
        openai_api_key=api_key
    )

def create_agent_chain(llm, prompt_template):
    """
    Creates a simple chain for an agent.
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)
    chain = (
        {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain
