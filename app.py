import streamlit as st

from src.faq_engine import find_best_answer
from src.logger import log_question


st.set_page_config(
    page_title="Urban Threads Co. FAQ Chatbot",
    page_icon="👕",
    layout="centered"
)

st.title("Urban Threads Co. FAQ Chatbot")
st.write("Ask a question about shipping, returns, exchanges, payments, sizing, or orders.")

st.info("This assistant answers only from the Urban Threads Co. FAQ knowledge base.")

user_question = st.text_input("Type your question here:")

if st.button("Ask"):
    if user_question.strip() == "":
        st.warning("Please type a question first.")
    else:
        result = find_best_answer(user_question)

        log_question(
            user_question=user_question,
            category=result["category"],
            status=result["status"]
        )

        st.subheader("Answer")
        st.write(result["answer"])

        st.caption(f"Category: {result['category']} | Status: {result['status']}")