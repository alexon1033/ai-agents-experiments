import os
from crewai import Agent
from langchain.agents import Tool

from langchain_community.utilities import GoogleSerperAPIWrapper
from crewai_tools import ScrapeWebsiteTool

os.environ['SERPER_API_KEY']='Kaf9cfc22ca2e7e5a4a091e3163204b93fec13706'

googleapiwrapper = GoogleSerperAPIWrapper()

search_tool = Tool(
    name="Search tool",
    func=googleapiwrapper.run,
    description="Useful for searching the internet"
)

scrape_tool = ScrapeWebsiteTool()

class BookDescriptionAgents():
    def researcher():
        return Agent(
            role="Book research analyst",
            goal="Find comprehenive information on a given book on the internet",
            backstory="""Seasoned book researcher and enthusiast with exertise in finding 
                        information about a book""",
            verbose=True,
            tools=[
                search_tool,
                scrape_tool
            ]
        )

    def describer():
        return Agent(
            role="Book description writer",
            goal="write book descriptions for a sales page. Make sure the descriptions are compelling yet factual.",
            backstory="""A descriptive writer who reads books and summarizes them into short 
                        paragraphs.""",
            verbose=True,
            tools=[
                search_tool,
                scrape_tool
            ]
        )

    def valuer():
        return Agent(
            role="Book salesman",
            goal="Value a book for second-hand sale.",
            backstory="""A book salesman who focuses on pricing books fairly and competitively
                         based on research. You run a business and need to make sure you sell 
                         a book in good time but not too cheap.""",
            tools=[
                search_tool,
                scrape_tool
            ]
        )
