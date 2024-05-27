from textwrap import dedent
from crewai import Task

class HomeworkCorrectionTasks():
    def project_initiation_task(self, agent, student_answer, education_resources):
        return Task(
            description=dedent(f"""
            Initiate the homework correction project by reviewing the project scope and student requirements. Develop a project plan that includes timelines, analysis requirements, and task assignments.
            Student Answer: {student_answer}
            """),
            expected_output=dedent("""
            A comprehensive project plan that outlines the project timeline, analysis 
            requirements, and task assignments for each team member.
            """),
            async_execution=True,
            agent=agent,
            tools=[education_resources.query_chroma]
        )

    def textbook_analysis_task(self, agent, student_answer, education_resources):
        return Task(
            description=dedent(f"""
            Analyze the textbook content and identify the chapters related to the student's incorrect answers.
            Student Answer: {student_answer}
            """),
            expected_output=dedent("""
            A detailed report containing textbook analysis results, indicating the 
            chapters related to the student's incorrect answers.
            """),
            async_execution=True,
            agent=agent,
            tools=[education_resources.query_chroma]
        )

    def homework_grading_task(self, agent, student_answer):
        return Task(
            description=dedent(f"""
            Grade the student's homework and compile explanations of their incorrect concepts. Output the results as a .md file.
            Student Answer: {student_answer}
            """),
            expected_output=dedent("""
            A .md file summarizing the homework grading results, focusing on the 
            student's incorrect concepts and explanations.
            """),
            async_execution=True,
            agent=agent
        )

    def error_book_creation_task(self, agent, student_answer, education_resources):
        return Task(
            description=dedent(f"""
            Based on the student's misconceptions, search for relevant college entrance exam questions and compile them into an error book. Output the error book as a .md file.
            Student Answer: {student_answer}
            """),
            expected_output=dedent("""
            A .md file containing the error book, which includes relevant college 
            entrance exam questions based on the student's misconceptions.
            """),
            agent=agent,
            tools=[education_resources.query_chroma]
        )

    def final_report_task(self, agent, student_answer, education_resources):
        return Task(
            description=dedent(f"""
            Review and consolidate the results from the textbook analysis, homework grading, and error book creation. Prepare a final report that provides an overall assessment of the student's homework, identifies misconceptions, and includes the error book.
            Student Answer: {student_answer}
            """),
            expected_output=dedent("""
            A comprehensive final report that includes textbook analysis, homework 
            grading results, error book, and overall recommendations for the student's 
            homework.
            """),
            agent=agent,
            tools=[education_resources.query_chroma]
        )