from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from typing import List
from pydantic import BaseModel, Field

load_dotenv()

class Source(BaseModel):
    """Schema for a source used by the agent"""

    url:str = Field(description='The url of the source')

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer:str = Field(description="The agent's answer to the querry")
    sources: List[Source] = Field(default_factory=list, description="list of the sources used to generate the answer")



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
agent = create_agent(model=llm,tools=tools,response_format=AgentResponse)

def main():
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job openings in south india for lanchain agntic AI developers for 1 year work experience individuals?")})
    print(result)
