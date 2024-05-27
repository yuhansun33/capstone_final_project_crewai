from textwrap import dedent
from crewai import Task
from chroma import query_chroma

class HomeworkCorrectionTasks():
    def project_initiation_task(self, agent, student_answer):
        return Task(
            description=dedent(f"""
            透過審查專案範圍和學生需求來啟動作業批改專案。制定一個包含分析要求和任務分配的專案計劃。
            學生的問題和他的答案：{student_answer}
            """),
            expected_output=dedent("""
            一份全面的專案計劃，概述專案、分析要求以及每個團隊成員的任務分配。
            """),
            async_execution=True,
            agent=agent,
            tools=[query_chroma]
        )

    def textbook_analysis_task(self, agent, student_answer):
        return Task(
            description=dedent(f"""
            分析教科書內容，並確定與學生錯誤答案相關的章節。
            學生的問題和他的答案：{student_answer}
            """),
            expected_output=dedent("""
            一份詳細的報告，包含教科書分析結果，指出與學生錯誤答案相關的章節。
            """),
            async_execution=True,
            agent=agent,
            tools=[query_chroma]
        )

    def homework_grading_task(self, agent, student_answer):
        return Task(
            description=dedent(f"""
            批改學生的作業，並彙整他們錯誤概念的解釋，並補充相關其他也可能錯誤的章節類似題目。
            學生的問題和他的答案：{student_answer}
            """),
            expected_output=dedent("""
            總結作業批改結果，重點關注學生的錯誤概念和解釋。
            """),
            async_execution=True,
            agent=agent,
            tools=[query_chroma]
        )

    def error_book_creation_task(self, agent, student_answer):
        return Task(
            description=dedent(f"""
            根據學生的錯誤概念，搜尋相關的大學入學考試題目，並將其彙整為錯題本。將錯題本輸出為 .md 檔案。
            學生的問題和他的答案：{student_answer}
            """),
            expected_output=dedent("""
            一個 .md 檔案，包含根據學生錯誤概念而編製的錯題本，其中包括相關的大學入學考試題目。
            """),
            agent=agent,
            tools=[query_chroma]
        )

    def final_report_task(self, agent, student_answer):
        return Task(
            description=dedent(f"""
            審查並整合教科書分析、作業批改和錯題本創建的結果。準備一份最終報告，提供對學生作業的總體評估，識別錯誤概念，並包含錯題本。
            學生的問題和他的答案：{student_answer}
            """),
            expected_output=dedent("""
            一份全面的最終報告，包括教科書分析、作業批改結果、錯題本以及對學生作業的整體建議。
            """),
            agent=agent,
            tools=[query_chroma]
        )