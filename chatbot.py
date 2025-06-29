import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)

st.header("Gemini Chatbot")
st.caption("Powered by LangChain + Gemini 2.0")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.chat_history.append(user_input)

    result = model.invoke(st.session_state.chat_history)

    st.session_state.chat_history.append(result.content)

for i, message in enumerate(st.session_state.chat_history):
    is_user = i % 2 == 0  # Even index = user, odd = AI
    with st.chat_message("user" if is_user else "assistant"):
        st.markdown(message)
