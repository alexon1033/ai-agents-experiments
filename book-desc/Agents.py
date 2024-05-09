from crewai import Agent

from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

class BookDescriptionAgents():
    def researcher():
        return Agent(
            role="Book research analyst",
            goal="Find comprehenive information on a given book on the internet",
            backstory="""Seasoned book researcher and enthusiast with exertise in finding 
                        information about a book""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet
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
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet
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
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet
            ]
        )
