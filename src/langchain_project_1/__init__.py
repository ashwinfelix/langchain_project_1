from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()

@tool
def search(querry: str) -> str:
    """
    Tool that searches over internet
    Args:
        querry: The querry to search for
    Returns:
        The search result
    """
    print(f"Searching for {querry}")
    return tavily.search(query=querry)

llm = ChatOpenAI(model="gpt-5")
tools = [search]
agent = create_agent(model=llm,tools=tools)

def main():
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job openings in south india for lanchain agntic AI developers for 1 year work experience individuals?")})
    print(result)
