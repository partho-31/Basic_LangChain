from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.8-flash"
)

st.header("Chatbot")


user_input = st.chat_input("Type your message")

if user_input:
    if user_input.strip().lower() == 'exit':
        st.stop()

    with st.chat_message("user"):
        st.write(user_input)

    result = model.invoke(user_input)


    with st.chat_message('assistant'):
        st.write(result.content[0]["text"])

