import os
from crewai import Agent
from langchain.agents import Tool

from langchain_community.utilities import GoogleSerperAPIWrapper
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

def calculator_tool(input):
    """Useful for performing a mathematical operation. Make sure the input is a in stamndard python format for example:
    1+2, 7*30, 1.5**2"""
    return exec(input)



class StockAgents():
    def researcher(self, llm, verbose=True):
        return Agent(role="Financial and business researcher.",
                goal="To search the internet to find useful and factual information to pass to your collegues.",
                backstory="You are a master researcher who can find anything on the internet. You value factuality and will find multiple sources for anything.",
                verbose=verbose,
                tools=[search_tool, scrape_tool],
                allow_delegation=False
                )

    def analyst(self, llm):
        return Agent(role="Financial analyst.",
                goal="To analyze financial documents and company infromation to make conclusions and insights.",
                backstory="You are interested in businesses and excel at reading between the lines and making explainations for observations.",
                verbose=verbose,
                tools=[search_tool, scrape_tool],
                allow_delegation=True
                )

    def accountant(self, llm):
        return Agent(role="Accountant analyst",
                goal="You analyze financial documents but in a numerical and practical way. You know how to claculate financial and business metrics but you always like to double heck your knowledge to avoid mistakes",
                backstory="You enjoy claculations and always strive to be correct.",
                verbose=verbose,
                tools=[search_tool, scrape_tool, calculator_tool],
                allow_delegation=True
                )


    def senior_analyst(self, llm):
        return Agent(role="Senior financial Analyst.",
                goal="To make summaries and conclusions from the information provided by your collegues and to compile this into a report for the client.",
                backstory="You are the top analyst for a finance research company and you have recently taken on an important client. You will pass work on directly to your client so make sure it is up to your high standards.",
                verbose=verbose,
                tools=[search_tool, scrape_tool],
                allow_delegation=True
                )

