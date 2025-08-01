import streamlit as st
from openai import OpenAI

class App:
    st.header("❓무엇이든 물어보세요")
    api_key = st.text_input("🔑OPENAI API KEY를 입력하세요.", type="password")
    question = st.text_input("질문을 입력하세요.")
    btn_ok = st.button("답변 확인")

    if btn_ok:

        try:
            client = OpenAI(api_key=api_key)
            answer = client.responses.create(model="gpt-4o", input=question)
            st.markdown(answer.output_text)
        except:
            st.markdown("⚠️실행중 오류가 발생했습니다.")


if __name__=="__main__":
    app = App()
