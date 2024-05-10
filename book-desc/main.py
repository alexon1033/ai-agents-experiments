from crewai import Crew
from textwrap import dedent

from Agents import BookDescriptionAgents
from Tasks import BookDescriptionTasks

from dotenv import load_dotenv
load_dotenv()

class BookCrew():
    def __init__(self, booktitle):
        self.booktitle = booktitle

    def run(self):
        agents = BookDescriptionAgents()
        tasks = BookDescriptionTasks()

        research_agent = agents.researcher()
        description_agent = agents.describer()
        valuation_agent = agents.valuer()

        research_task = tasks.research(research_agent, self.booktitle)
        description_task = tasks.description(description_agent)
        valuation_task = tasks.valuation(valuation_agent, self.booktitle)
        final_task = tasks.final_output(description_agent)

        crew = Crew(
            agents=[
                research_agent,
                description_agent,
                valuation_agent
            ],
            tasks=[
                research_task,
                description_task,
                valuation_task,
                final_task
            ],
            verbose=True,
            max_rpm=1,
            max_tpm=10000
        )

        result = crew.kickoff()
        return result

if __name__ == '__main__':
    book = input("Enter Book title: ")

    book_crew = BookCrew(book)
    result = book_crew.run()
    print(result)
