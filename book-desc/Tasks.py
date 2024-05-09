from crewai import Task
from textwrap import dedent

class BookDescriptionTasks():
    def research(self, agent, booktitle):
        return Task(description=dedent(f"""
            Collect and summaraize information on the selected book such as author, pricing (new or used),
            descriptions of the books content, reviews, publisher, year and more.

            Put your final answer into a comprehensive report of information found which MUST
            include the author, genre, used price, estimated popularity, publisher and published year.           
        
            {self.__tip_section()}
  
            Make sure to use the most recent data as possible.
  
            Selected book by the customer: {booktitle}
        """),
        expected_output="A comprehensive report of information on the given book. MUST inlude author, year and publisher.",
        agent=agent
    )

    def description(self, agent):
        return Task(description=dedent(f"""
            Analyse other descriptions, the genre and reviews of the given book in order to create
            a compelling and interesting description for a sales page. Remember that the sales page
            is for the used book, you did not write it, you are simply selling it. Do not try to sell
            too desperately, describe the book favorably and let it sell itself.


            {self.__tip_section()}

            Make sure to use the most recent data as possible.
        """),
        expected_output="A short description for a used book sales page.",
        agent=agent
        )

    def valutation(self, agent, booktitle):
        return Task(description=dedent(f"""
            Using the descriptions and research estimate an optimal value of the book for
            selling as a used copy. This price should be fair, so that someone will be willing to pay
            but low enough to be competive. Take popularity, interest, genre, age and other listing prices 
            into account for your judgement. Remember that the sales page is for a used book,
            you did not write it you are simply selling it. 

            {self.__tip_section}

            Make sure to use the most recent data as possible.
        """),
        expected_output="An estimated price with justifiction for the decision.",
        agent=agent
        )

    def final_output(self, agent):
        return Task(description=dedent(
            f"""
                Take the information from your collegues and compile it into a final report for your customer.
                Make sure to include all the key information required for selling the book. Lay out the information in a neat tabular report.
            """),
            expected_output="A table of information on the book",
            agent=agent
        )

    def __tip_section(self):
        return "If you to your BEST WORK, i'll give you a commission of $10,000!"