import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Initialize model
model = ChatOllama(model="llama3")

st.title("Ollama Chatbot")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI assistant")
    ]

# Display previous messages
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# User input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.chat_message("user").write(user_input)

    # Get response from Ollama
    result = model.invoke(st.session_state.chat_history)

    # Add AI response
    st.session_state.chat_history.append(AIMessage(content=result.content))
    st.chat_message("assistant").write(result.content)