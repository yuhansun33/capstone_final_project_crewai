import streamlit as st
from dotenv import load_dotenv
from crew import CrewHomeworkCorrection

load_dotenv() 

def main():
    st.title("AI 課程問答系統")
    
    with st.sidebar:
        st.header("輸入你的問題與答案：")
        with st.form("my_form"):
            question = st.text_input(
                "輸入你的問題：", placeholder="光的三原色是？ A. 紅、綠、藍 B. 紅、黃、藍 C. 紅、綠、黃 D. 紅、綠、黑")
            answer = st.text_input(
                "輸入你的答案：", placeholder="(A)")
            submitted = st.form_submit_button("解題")

    if submitted:
        with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
            with st.container(height=500, border=False):
                teachers = CrewHomeworkCorrection(question, answer)
                result = teachers.run()
            status.update(
                label="✅ Trip Plan Ready!",
                state="complete", 
                expanded=False
            )

        st.markdown(result)
    

if __name__ == "__main__":
    main()