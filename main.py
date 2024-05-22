from dotenv import load_dotenv

load_dotenv()

from crewai import Crew, Process
from tasks import AnalysisPreparationTasks
from agents import AnalysisPreparationAgents

tasks = AnalysisPreparationTasks()
agents = AnalysisPreparationAgents()

print("## Welcome to the Analysis Prep Crew")
print('-------------------------------')

product_description = input("Please provide the product description (name, purchasing channel, condition, etc.):\n")
price = input("Please provide the price of the product:\n")

# Create Agents
program_manager_agent = agents.program_manager_agent()
product_analyst_agent = agents.product_analyst_agent()
review_analyst_agent = agents.review_analyst_agent()
fraud_detection_agent = agents.fraud_detection_agent()

# Create Tasks
project_initiation = tasks.project_initiation_task(program_manager_agent, product_description, price)
product_analysis = tasks.product_analysis_task(product_analyst_agent, product_description)
review_analysis = tasks.review_analysis_task(review_analyst_agent, product_description)
fraud_assessment = tasks.fraud_assessment_task(fraud_detection_agent, product_description, price)
final_report = tasks.final_report_task(program_manager_agent, product_description, price)

fraud_assessment.context = [product_analysis, review_analysis]
final_report.context = [product_analysis, review_analysis, fraud_assessment]

# Create Crew responsible for Analysis
crew = Crew(
    agents=[
        program_manager_agent,
        product_analyst_agent,
        review_analyst_agent,
        fraud_detection_agent
    ],
    tasks=[
        project_initiation,
        product_analysis,
        review_analysis,
        fraud_assessment,
        final_report
    ],
    process = Process.sequential
)

result = crew.kickoff()

# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(result)