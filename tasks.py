from textwrap import dedent
from crewai import Task
from chroma import query_chroma

class HomeworkCorrectionTasks():
    def project_initiation_task(self, agent, student_answer):
        return Task(
            description=dedent(f"""
            透過審查專案範圍和學生需求來啟動團隊專案。制定一個包含分析要求和任務分配的專案計劃。
            學生的問題和他的答案：{student_answer}
            """),
            expected_output=dedent("""
            一份詳盡的專案計劃，概述專案、分析要求以及每個團隊成員的任務分配，並指定他們要給你對於學生有幫助的內容。
            """),
            async_execution=True,
            agent=agent,
        )

    def textbook_analysis_task(self, agent, student_answer):
        return Task(
            description=dedent(f"""
            分析教科書內容，並確定與學生錯誤答案相關的章節。
            學生的問題和他的答案：{student_answer}
            """),
            expected_output=dedent("""
            一份詳細的報告，包含教科書分析結果，指出與學生錯誤答案相關的章節，必要知識點和學習重點，並回傳給導師整理訊息。
            """),
            async_execution=True,
            agent=agent,
            tools=[query_chroma]
        )

    def homework_grading_task(self, agent, student_answer):
        return Task(
            description=dedent(f"""
            批改學生的作業，並彙整他們錯誤概念的解釋，或是提出他們為什麼錯誤的易錯想法。
            學生的問題和他的答案：{student_answer}
            """),
            expected_output=dedent("""
            總結作業批改結果，重點關注學生的錯誤概念和解釋其落入怎樣的考題陷阱當中。
            """),
            async_execution=True,
            agent=agent,
            tools=[query_chroma]
        )

    def error_book_creation_task(self, agent, student_answer):
        return Task(
            description=dedent(f"""
            根據學生的錯誤概念，搜尋相關考試題目或習題，並將其彙整起來，回傳給導師整理。
            學生的問題和他的答案：{student_answer}
            """),
            expected_output=dedent("""
            包含根據學生錯誤概念而彙整的類似題型，或是同章節題目，其中包括其他試題和習題。
            """),
            agent=agent,
            tools=[query_chroma]
        )

    def final_report_task(self, agent, student_answer):
        return Task(
            description=dedent(f"""
            審查並整合教科書分析師、作業批改師和錯題整理師創建的結果。以他們的內容準備一份最終報告，提供對學生作業的總體評估，教科書章節與概念，並包含相近錯誤題型。
            學生的問題和他的答案：{student_answer}
            """),
            expected_output=dedent("""
            一份全面的最終報告，在審閱教科書分析、作業批改結果、錯題本以及對學生作業的整體建議過後，以精確並保留重要資訊的情況下，並以 .md 檔輸出。
            """),
            agent=agent,
            tools=[query_chroma]
        )