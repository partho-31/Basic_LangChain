from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    max_new_tokens=500,
)

model = ChatHuggingFace(llm = llm)

st.header("ChatBot")

# Declaring state for managing chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Displaying chat history
for message in st.session_state.chat_history:
        role = "assistant" if isinstance(message,AIMessage) else "user"
        if role == 'user':
             with st.chat_message(role):
                  st.write(message.content)
        else:
            with st.chat_message(role):
              st.write(message.content)


# print chat history
with st.sidebar:
    st.subheader("Chat History")
    if not st.session_state.chat_history:
        st.write("(empty)")
    else:
        for msg in st.session_state.chat_history:
            role = "AI" if isinstance(msg, AIMessage) else "Human"
            st.write(f"**{role}:** {msg.content}")


# Input logic
user_input = st.chat_input("Type your throughts!")

if user_input:
    if user_input.strip().lower() == 'exit':
        st.stop()
    
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message('user'):
        st.write(user_input)

    response = model.invoke(st.session_state.chat_history)
    
    st.session_state.chat_history.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)
    

    



