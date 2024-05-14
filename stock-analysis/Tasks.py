from crewai import Task
from textwrap import dedent

def __tip_section():
    return dedent("""
        You have access to the internet. Use the search tool to find websites and use the scrape tool to extract data from them. Only use information you find online or is given to you,
        do not make up information as you could lose your job. Always fact check your ideas or infromation given to you by collegues using the internet.
        
        If you do your BEST WORK ill give you a bonus of $10,000!
        """)

class StockTasks():
    def collect_company_information(self, agent, company):
        return Task(description=dedent(f"""
            Task: Collect comprehensive information about a specific company.
            
            Company Name: {comapny} 

            Instructions:
            General Overview: Provide a brief introduction to the company, including its founding year, founders, and headquarters location.

            Business Model: Describe the primary business model of the company. What products or services do they offer? Who are their main customers?

            Key Financials: Gather recent financial data such as annual revenue, profit margins, and market capitalization (if publicly traded).

            Management Team: List key members of the executive team and their roles within the company.

            Competitive Landscape: Identify main competitors and describe how the company differentiates itself in the market.

            Recent News: Find any recent news articles or press releases about the company from the last six months to provide context on recent developments.

            Challenges and Opportunities: Analyze any major challenges the company is currently facing or opportunities it might be positioned to take advantage of.

            Future Outlook: Provide insights on the company's future direction based on recent announcements or market trends..
            
            Sources: Utilize reputable business news websites, the company's official website, financial databases, and industry reports to gather information.
            Ensure all data is up-to-date and cite sources accordingly. 

            {__tip_section()}
            """),
            expected_output="Present the information in a structured report format, with clear headings for each section and bullet points for key details. Include hyperlinks to sources where applicable.",
            agent=agent
        )

    def collect_financial_statements(self, agent, company):
        return Task(description=dedent(f"""
            Objective: Your task is to collect comprehensive financial statements for a specific company for the last five fiscal years. You will need to access balance
            sheets, income statements, and cash flow statements.

            Company Name: {comapny}

            Instructions:
            Identify the Company: Confirm the exact name and details of the company for which financial statements are needed.
            Make sure to clarify any potential ambiguities regarding the company's name or its subsidiaries.

            Source Documents: Use authoritative financial databases like Bloomberg, Yahoo Finance, or the company’s own investor relations website.Ensure that the
            documents pertain to the last five fiscal years.Confirm that the documents are the most recent and have been audited or reviewed by a reputable third party,
            if applicable.

            Document Retrieval: Download the annual reports or 10-K filings which contain the comprehensive financial statements.If necessary, also retrieve quarterly
            reports or 10-Q filings for the most recent fiscal year.

            Verification: Check the date and completeness of each financial statement. Ensure all parts of each statement are legible and in a standardized format,
            preferably PDF or Excel.

            Organize and Compile: Organize the documents by fiscal year.

            Report Back: Summarize the retrieval process. Provide information about the balance sheets, cashflow and any other information of note to your collegues.

            {__tip_section()}
            """),
            expected_output="You should provide a comprehensive collection of financial statements organized by type and fiscal year, with a clear summary of your process and any observations or discrepancies noted during the collection.",
            agent=agent
        )

    def research_market_and_trends(self, agent, company):
        return Task(description=dedent(f"""
            You are tasked with performing comprehensive market research on the company {company}. 
            Your goal is to provide a detailed analysis that includes the following aspects:
            
            Company Overview: Brief history of the company.Main products or services offered.Key markets and geographical presence.

            Industry Analysis: Identify the industry in which the company operates.Discuss the current trends affecting this industry.Analyze the competitive landscape, 
            including major competitors.

            Financial Performance: Review the latest available financial data for the company (e.g., revenue, profit margins, growth rates).
            Compare these figures with industry averages or key competitors.

            Customer and Market Analysis: Describe the company's target customer demographics.Assess the size and growth potential of the market.
            Evaluate customer perceptions and satisfaction related to the company's products or services.

            SWOT Analysis (Strengths, Weaknesses, Opportunities, Threats): Identify and explain internal strengths and weaknesses of the company.
            Discuss external opportunities and threats that could impact the company's success.

            Regulatory and Environmental Factors: Outline any significant regulatory challenges facing the company or its industry.
            Discuss any environmental sustainability practices or policies the company has adopted.

            Technology and Innovation: Evaluate the company's use of technology and its role in competitive positioning.Highlight any recent or upcoming
            technological advancements that could affect the company.
            
            Recommendations:Based on your analysis, suggest strategic actions the company could take to improve its market position and financial performance.

            Guidelines for Response: Provide well-researched, accurate, and up-to-date information. Use credible sources and data to support your analysis.

            Maintain an objective and analytical tone throughout the report. Ensure that all information is clear, concise, and logically organized.

            {__tip_section()}
            """),
            expected_output="A market ananlysis report Ensure that all information is clear, concise, and logically organized.",
            agent=agent,
            context=[self.collect_company_information, self.collect_financial_statements]
        )

    def analyze_financial_statements(self, agent, company):
        return Task(description=dedent(f"""
            1. Gather and Organize the Financial Statements.
            Ensure you have the three core financial statements:
            
            Income Statement: Provides a summary of the company's revenues, expenses, and profits over a period.

            Balance Sheet: Shows the company's assets, liabilities, and equity at a specific point in time.
            Cash Flow Statement: Offers details on the inflow and outflow of cash from operating, investing, and financing activities.
            
            2. Perform Horizontal and Vertical Analysis.

            Horizontal Analysis: Compare the financial data across multiple periods to identify trends and growth patterns.Calculate the change in each line
            item year over year.Express these changes as a percentage to assess significant trends.
            
            Vertical Analysis: Analyze each item as a percentage of a base figure within a single period.For the income statement, express each item as a 
            percentage of total revenues.For the balance sheet, express each item as a percentage of total assets or total liabilities plus equity.
            
            3. Analyze Cash Flows
            Assess the cash flows from operating activities to understand the cash generated from business operations.Evaluate investing activities for insights
            into cash spent on and generated from investments like property, plant, and equipment.
             
            Review financing activities to see how the company raises capital and returns value to shareholders through dividends and stock buybacks.
             
            4. Compare Against Benchmarks Industry Comparisons: Compare the company's performance with industry averages to gauge its relative position.
            Historical Performance: Compare current findings against historical data to assess performance trends.

            Peer Analysis: Compare financial metrics with close competitors to understand competitive positioning.
            
            6. Conduct Qualitative Analysis
            Management Discussion and Analysis (MD&A): Review this section in the annual report for management's perspective on the financial results and what drives them.

            Notes to the Financial Statements: Provides essential details that complement the figures on the financial statements, such as accounting policies,
            contingencies, and risk management.
            
            {__tip_section()}
            """),
            expected_output=dedent("""7. Prepare a Written Report
            Compile your findings into a structured report that includes:

            Executive Summary: Overview of the financial health and performance trends.

            Detailed Analysis: Comprehensive details of your analyses, supported by charts and graphs.
            
            Conclusions and Recommendations: Final assessment of the financial health, potential concerns, and strategic recommendations."""),
            context=[self.collect_company_information, self.collect_financial_statements],
            agent=agent
    )

    def calculate_financial_ratios(self, agent, company):
        return Task(description=dedent(f"""
            Calculate Key Financial Ratios.

            Focus on the following categories of ratios for a comprehensive analysis:
            Liquidity Ratios (e.g., Current Ratio, Quick Ratio): Measure the company’s ability to meet short-term obligations.
            
            Solvency Ratios (e.g., Debt to Equity, Interest Coverage): Assess the company’s long-term solvency and debt levels.

            Profitability Ratios (e.g., Gross Profit Margin, Return on Equity): Evaluate the company’s efficiency in using its resources to generate profits.

            Efficiency Ratios (e.g., Asset Turnover, Inventory Turnover): Examine how effectively the company uses its assets.

            {__tip_section()}
            """),
            expected_ouput="A list of financial ratios for the given company name and an interpretation of each.",
            context=[self.collect_financial_statements],
            agent=agent
        )

    def summarize(self, agent):
        return Task(description=dedent(f"""
            Summarize the information you have been provided with into a concice report. Make sure to stick to the facts and make
            each point only once. Make sure to include all the important details. 

            {__tip_section()}   
            """),
            expected_output="A report summarizing all the facts.",
            agent=agent,
            context=[self.calculate_financial_ratios, self.analyze_financial_statements]
        )

    def draw_conslusions():
        return Task(description=dedent(f"""
            Using the infromation provided to you by the summary report on the company, use your business knowledge to draw conclusions and make preictions with this information.

            {__tip_section()}
            """),
            expected_output="Place your consclusions and forecasts in a single report and justify each point.",
            agent=agent,
            context=[self.summarize])

    def make_recommendation():
        return Task(description=dedent(f"""
            Make a final report for the customer. This report must contain a recommendation to buy, hold or sell based on the infromation you have been provided.
            Add justifications to make sure the customer understands why you make your recommendation.

            {__tip_section}
            """),
            expected_output=dedent("""A final report for the customer. Must contain a recommendation to buy, sell or hold based on your reasoning. Make sure it is comprehensive 
            and readable. Make it pretty for your customer/"""),
            agent=agent,
            context=[self.draw_conclusions]
        )

