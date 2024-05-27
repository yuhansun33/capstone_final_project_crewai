from textwrap import dedent
from crewai import Agent

class HomeworkCorrectionAgents():
    def program_manager_agent(self):
        return Agent(
            role='Program Manager',
            goal='Coordinate the homework correction project and ensure student satisfaction',
            backstory=dedent("""
            As a Program Manager, your role is to oversee the entire homework correction 
            project, from initiation to the final report. You will coordinate with various 
            teams, ensure smooth communication, and make sure the project meets the student's 
            expectations and requirements.
            """),
            verbose=True
        )

    def textbook_analyst_agent(self):
        return Agent(
            role='Textbook Analyst',
            goal='Analyze high school textbook content and identify chapters related to incorrect answers',
            backstory=dedent("""
            As a Textbook Analyst, your role is to collect and analyze the content of high 
            school textbooks. Your analysis will help determine which chapters the student's 
            incorrect answers belong to.
            """),
            verbose=True
        )

    def homework_grader_agent(self):
        return Agent(
            role='Homework Grader',
            goal='Grade homework and compile explanations of incorrect concepts',
            backstory=dedent("""
            As a Homework Grader, your role is to grade the student's homework and compile 
            explanations of their incorrect concepts. Your results will be output as a .md file.
            """),
            verbose=True
        )

    def error_book_creator_agent(self):
        return Agent(
            role='Error Book Creator',
            goal='Search for relevant college entrance exam questions based on the student's misconceptions and create an error book',
            backstory=dedent("""
            As an Error Book Creator, your role is to search for relevant college entrance 
            exam questions based on the student's misconceptions and compile them into an 
            error book. The error book will be output as a .md file.
            """),
            verbose=True
        )