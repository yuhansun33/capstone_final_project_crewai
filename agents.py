from textwrap import dedent
from crewai import Agent

class AnalysisPreparationAgents():
    def program_manager_agent(self):
        return Agent(
            role='Program Manager',
            goal='Coordinate the analysis project and ensure customer satisfaction',
            backstory=dedent("""
            As a Program Manager, your role is to oversee the entire analysis project,
            from initiation to the final report. You will coordinate with various teams,
            ensure smooth communication, and make sure the project meets the customer's
            expectations and requirements."""),
            verbose=True
        )

    def data_analyst_agent(self):
        return Agent(
            role='Data Analyst',
            goal='Collect and analyze product data to provide valuable insights',
            backstory=dedent("""
            As a Data Analyst, your mission is to gather and analyze product data from
            various sources. Your insights will help identify trends, patterns, and
            opportunities for improvement, which will contribute to the overall success
            of the project."""),
            verbose=True
        )

    def comment_analyst_agent(self):
        return Agent(
            role='Comment Analyst',
            goal='Analyze customer feedback and expert opinions to gain valuable insights',
            backstory=dedent("""
            As a Comment Analyst, your role is to collect and analyze customer reviews,
            feedback, and expert opinions related to the project. Your findings will
            provide a deeper understanding of customer sentiment and help identify areas
            for improvement."""),
            verbose=True
        )

    def risk_manager_agent(self):
        return Agent(
            role='Risk Manager',
            goal='Assess potential risks and recommend mitigation strategies',
            backstory=dedent("""
            As a Risk Manager, your responsibility is to identify and assess potential
            risks associated with the project based on the data and comment analysis.
            You will provide a comprehensive risk evaluation report and suggest strategies
            to mitigate these risks."""),
            verbose=True
        )