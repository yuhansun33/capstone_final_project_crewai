from textwrap import dedent
from crewai import Agent
from chroma import query_chroma

class HomeworkCorrectionAgents():
    def program_manager_agent(self):
        return Agent(
            role='導師',
            goal='協調作業批改專案並確保學生滿意度、以及學習成效',
            backstory=dedent("""
            作為項目經理，你的職責是監督整個作業批改專案，從啟動到最終報告。你將與各個團隊協調，確保順暢的溝通，並確保專案符合學生的期望和要求。
            """),
            tools=[query_chroma],
            verbose=True
        )

    def textbook_analyst_agent(self):
        return Agent(
            role='教科書分析師',
            goal='分析學生問題，並依照高中教科書，指出問題和答案相關或是所屬的章節',
            backstory=dedent("""
            作為教科書分析師，你的職責是收集和分析高中教科書的內容。你的分析將有助於確定學生的錯誤答案所屬的章節。
            """),
            tools=[query_chroma],
            verbose=True
        )

    def homework_grader_agent(self):
        return Agent(
            role='作業批改員',
            goal='批改作業並彙整錯誤概念的解釋',
            backstory=dedent("""
            作為作業批改員，你的職責是批改學生的作業，並彙整他們錯誤概念的解釋。你的結果將輸出為 .md 檔案。
            """),
            tools=[query_chroma],
            verbose=True
        )

    def error_book_creator_agent(self):
        return Agent(
            role='錯題本創建者',
            goal='根據學生的錯誤概念搜尋相關的大學入學考試題目，並創建錯題本',
            backstory=dedent("""
            作為錯題本創建者，你的職責是根據學生的錯誤概念搜尋相關的大學入學考試題目，並將其彙整為錯題本。錯題本將輸出為 .md 檔案。
            """),
            tools=[query_chroma],
            verbose=True
        )