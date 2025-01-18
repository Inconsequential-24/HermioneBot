import streamlit as st
from chatbot.chatbot import HermioneChatbot

# Initialize the chatbot
chatbot = HermioneChatbot()

st.title("Hermione Granger Chatbot")

# User input field
user_input = st.text_input("Ask Hermione something:")

if user_input:
    response = chatbot.get_response(user_input)
    st.write(f"Hermione: {response}")