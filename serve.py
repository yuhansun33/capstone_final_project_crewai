import streamlit as st

# 清空輸入框，複製到問題欄
def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""

# 當使用者按下送出按鈕或按下 Enter 鍵時，設定 send_input 為 True，呼叫 clear_input_field 函式
def set_send_input():
    st.session_state.send_input = True
    clear_input_field()

def main():
    st.title("AI 課程問答系統")
    # div
    chat_container = st.container()
    
    # 如果 session_state 中沒有 send_input 和 user_question，則初始化為 False 和空字串
    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""
    
    # 輸入框
    user_input = st.text_input("輸入你的問題", key = "user_input", on_change = set_send_input)
    
    # 送出按鈕
    send_button = st.button("送出", key = "send_button")
    
    if send_button or st.session_state.send_input:
        if st.session_state.user_question != "":
            llm_response = "老師這麼說："
            with chat_container:
                st.chat_message("user").write(st.session_state.user_question)
                st.chat_message("ai").write("this is the answer")
    
if __name__ == "__main__":
    main()
    