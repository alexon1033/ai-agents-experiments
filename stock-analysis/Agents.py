import os
from crewai import Agent
from langchain.agents import Tool

from langchain_community.utilities import GoogleSerperAPIWrapper
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

class DataGatheringAgents():
    def 