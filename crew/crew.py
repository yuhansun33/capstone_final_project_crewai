from dotenv import load_dotenv

load_dotenv()

from crewai import Crew, Process
from tasks import AnalysisPreparationTasks
from agents import AnalysisPreparationAgents
from state import graphState


class CrewAnalysis():
    def __init__(self):
        print("## Welcome to the Analysis Prep Crew")
        print('-------------------------------')

        product_description = input("Please provide the product description (name, purchasing channel, condition, etc.):\n")
        price = input("Please provide the price of the product:\n")

        tasks = AnalysisPreparationTasks()
        agents = AnalysisPreparationAgents()

        # Create Agents
        self.program_manager_agent = agents.program_manager_agent()
        self.product_analyst_agent = agents.product_analyst_agent()
        self.review_analyst_agent = agents.review_analyst_agent()
        self.fraud_detection_agent = agents.fraud_detection_agent()

        # Create Tasks
        self.project_initiation = tasks.project_initiation_task(self.program_manager_agent, product_description, price)
        self.product_analysis = tasks.product_analysis_task(self.product_analyst_agent, product_description)
        self.review_analysis = tasks.review_analysis_task(self.review_analyst_agent, product_description)
        self.fraud_assessment = tasks.fraud_assessment_task(self.fraud_detection_agent, product_description, price)
        self.final_report = tasks.final_report_task(self.program_manager_agent, product_description, price)

        self.fraud_assessment.context = [self.product_analysis, self.review_analysis]
        self.final_report.context = [self.product_analysis, self.review_analysis, self.fraud_assessment]

    def run(self, state):

        # Create Crew responsible for Analysis
        crew = Crew(
            agents=[
                self.program_manager_agent,
                self.product_analyst_agent,
                self.review_analyst_agent,
                self.fraud_detection_agent
            ],
            tasks=[
                self.project_initiation,
                self.product_analysis,
                self.review_analysis,
                self.fraud_assessment,
                self.final_report
            ],
            verbose=True,
            process = Process.sequential
        )

        result = crew.kickoff()

        # Print results
        print("\n\n################################################")
        print("## Here is the result")
        print("################################################\n")
        print(result)

        return result


# if __name__ == "__main__":
#     crew_analysis = CrewAnalysis()
#     state = graphState()
#     crew_analysis.run(state)