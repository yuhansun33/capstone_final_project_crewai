from dotenv import load_dotenv

load_dotenv()

from crewai import Crew, Process
from tasks import AnalysisPreparationTasks
from agents import AnalysisPreparationAgents

tasks = AnalysisPreparationTasks()
agents = AnalysisPreparationAgents()

print("## Welcome to the Analysis Prep Crew")
print('-------------------------------')

project_scope = input("What is the scope of the project?\n")
customer_requirements = input("What are the customer's requirements?\n")

# Create Agents
program_manager_agent = agents.program_manager_agent()
data_analyst_agent = agents.data_analyst_agent()
comment_analyst_agent = agents.comment_analyst_agent()
risk_manager_agent = agents.risk_manager_agent()

# Create Tasks
project_initiation = tasks.project_initiation_task(program_manager_agent, project_scope, customer_requirements)
product_data_analysis = tasks.product_data_analysis_task(data_analyst_agent, project_scope)
customer_feedback_analysis = tasks.customer_feedback_analysis_task(comment_analyst_agent, project_scope)
risk_assessment = tasks.risk_assessment_task(risk_manager_agent, project_scope)
final_analysis_report = tasks.final_analysis_report_task(program_manager_agent, project_scope, customer_requirements)

risk_assessment.context = [product_data_analysis, customer_feedback_analysis]
final_analysis_report.context = [product_data_analysis, customer_feedback_analysis, risk_assessment]

# Create Crew responsible for Analysis
crew = Crew(
    agents=[
        program_manager_agent,
        data_analyst_agent,
        comment_analyst_agent,
        risk_manager_agent
    ],
    tasks=[
        project_initiation,
        product_data_analysis,
        customer_feedback_analysis,
        risk_assessment,
        final_analysis_report
    ]
    process = Process.sequential
)

result = crew.kickoff()

# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(result)