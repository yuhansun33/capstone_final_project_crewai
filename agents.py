from textwrap import dedent
from crewai import Agent
from chroma import query_chroma
from outputFile import outputMD
from langchain_openai import ChatOpenAI
import streamlit as st 

def streamlit_callback(step_output):
    # This function will be called after each step of the agent's execution
    st.markdown("---")
    for step in step_output:
        if isinstance(step, tuple) and len(step) == 2:
            action, observation = step
            if isinstance(action, dict) and "tool" in action and "tool_input" in action and "log" in action:
                st.markdown(f"# Action")
                st.markdown(f"**Tool:** {action['tool']}")
                st.markdown(f"**Tool Input** {action['tool_input']}")
                st.markdown(f"**Log:** {action['log']}")
                st.markdown(f"**Action:** {action['Action']}")
                st.markdown(
                    f"**Action Input:** ```json\n{action['tool_input']}\n```")
            elif isinstance(action, str):
                st.markdown(f"**Action:** {action}")
            else:
                st.markdown(f"**Action:** {str(action)}")

            st.markdown(f"**Observation**")
            if isinstance(observation, str):
                observation_lines = observation.split('\n')
                for line in observation_lines:
                    if line.startswith('Title: '):
                        st.markdown(f"**Title:** {line[7:]}")
                    elif line.startswith('Link: '):
                        st.markdown(f"**Link:** {line[6:]}")
                    elif line.startswith('Snippet: '):
                        st.markdown(f"**Snippet:** {line[9:]}")
                    elif line.startswith('-'):
                        st.markdown(line)
                    else:
                        st.markdown(line)
            else:
                st.markdown(str(observation))
        else:
            st.markdown(step)


class HomeworkCorrectionAgents:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o"
        )
    
    def program_manager_agent(self):
        return Agent(
            role='導師',
            goal='協調底下的教科書分析師、作業批改員和錯題本創建者，確保學生能有最佳的學習體驗',
            backstory=dedent("""
            作為導師，你的職責是監督整個教育集團，從開始到最終報告給學生的報告。你將與各個團隊成員協調，確保順暢的溝通，並確保專案符合學生的期望和要求。
            將學生問題分配交給教科書分析師，請它們分析學生問題，並依照高中教科書，指出問題和答案相關或是所屬的章節。
            將學生的問題批改交給作業批改員，請它們批改作業並彙整錯誤概念的解釋。
            將學生的錯誤概念給錯題整理者，請它們根據學生的錯誤概念搜尋相關的大學入學考試題目。
            """),
            verbose=True,
            llm=self.llm,
            step_callback=streamlit_callback,
        )

    def textbook_analyst_agent(self):
        return Agent(
            role='教科書分析師',
            goal='分析學生問題，並依照教科書內容，指出相關章節',
            backstory=dedent("""
            作為教科書分析師，你的職責是收集和分析高中教科書的內容。你的分析將有助於確定學生的錯誤答案所屬的章節，
            並概述該章節需要的必要知識點和學習重點，並回傳給報告撰寫員整理訊息。
            """),
            tools=[query_chroma],
            verbose=True,
            llm=self.llm,
            step_callback=streamlit_callback,
        )

    def homework_grader_agent(self):
        return Agent(
            role='作業批改員',
            goal='批改作業並彙整錯誤概念的解釋',
            backstory=dedent("""
            作為作業批改員，你的職責是批改學生的問題與答案，分析學生問題，並彙整他們錯誤概念的解釋，並回傳給報告撰寫員整理訊息。
            """),
            tools=[query_chroma],
            verbose=True,
            llm=self.llm,
            step_callback=streamlit_callback,
        )

    def error_book_creator_agent(self):
        return Agent(
            role='錯題整理者',
            goal='根據學生的錯誤概念搜尋相關的考試、或是習作題目',
            backstory=dedent("""
            作為錯題整理者，你的職責是根據學生的錯誤概念搜尋相關的考試或是習作題目，並回傳給報告撰寫員整理訊息。
            """),
            tools=[query_chroma],
            verbose=True,
            llm=self.llm,
            step_callback=streamlit_callback,
        )
    
    def report_writer_agent(self):
        return Agent(
            role='報告撰寫員',
            goal='根據教科書分析師、作業批改員和錯題整理者的結果，撰寫最終報告',
            backstory=dedent("""
            作為報告撰寫員，你的職責是審查並整合教科書分析師、作業批改員和錯題整理者創建的結果。以他們的內容準備一份最終報告，提供對學生作業的總體評估，教科書章節與概念，並包含相近錯誤題型。
            """),
            tools=[query_chroma, outputMD],
            verbose=True,
            llm=self.llm,
            step_callback=streamlit_callback,
        )