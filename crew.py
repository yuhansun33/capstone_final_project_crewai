from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process
from tasks import HomeworkCorrectionTasks
from agents import HomeworkCorrectionAgents
from state import graphState

class CrewHomeworkCorrection():
    def __init__(self):
        print("## 歡迎來到 AI 大講堂 ##")
        print('-------------------------------')
        student_answer = input("輸入你要問的問題與答案： \n")
        # textbook_info = input("Please enter the high school textbook information: \n")
        # exam_questions = input("Please enter the college entrance exam questions: \n")

        # education_resources = EducationResources(textbook_info, exam_questions)

        tasks = HomeworkCorrectionTasks()
        agents = HomeworkCorrectionAgents()

        # Create Agents
        self.program_manager_agent = agents.program_manager_agent()
        self.textbook_analyst_agent = agents.textbook_analyst_agent()
        self.homework_grader_agent = agents.homework_grader_agent()
        self.error_book_creator_agent = agents.error_book_creator_agent()

        # Create Tasks
        self.project_initiation = tasks.project_initiation_task(self.program_manager_agent, student_answer)
        self.textbook_analysis = tasks.textbook_analysis_task(self.textbook_analyst_agent, student_answer)
        self.homework_grading = tasks.homework_grading_task(self.homework_grader_agent, student_answer)
        self.error_book_creation = tasks.error_book_creation_task(self.error_book_creator_agent, student_answer)
        self.final_report = tasks.final_report_task(self.program_manager_agent, student_answer)

        self.error_book_creation.context = [self.textbook_analysis, self.homework_grading]
        self.final_report.context = [self.textbook_analysis, self.homework_grading, self.error_book_creation]

    def run(self, state):
        # Create Crew responsible for Homework Correction
        crew = Crew(
            agents=[
                self.program_manager_agent,
                self.textbook_analyst_agent,
                self.homework_grader_agent,
                self.error_book_creator_agent
            ],
            tasks=[
                self.project_initiation,
                self.textbook_analysis,
                self.homework_grading,
                self.error_book_creation,
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

        # write the result to a markdown file
        output_file = "TeacherOutput.md"
        with open(output_file, "w") as file:
            file.write(result)
        
        return result

if __name__ == "__main__":
    crew_homework_correction = CrewHomeworkCorrection()
    state = graphState()
    crew_homework_correction.run(state)
