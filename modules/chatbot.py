import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel("gemini-2.5-flash")


def ask_ai(question):

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

   
    st.session_state.chat_history.append({
        "role": "user",
        "content": question
    })

    
    conversation = ""

    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            conversation += f"User: {chat['content']}\n"
        else:
            conversation += f"AI: {chat['content']}\n"

    prompt = f"""
You are an intelligent AI assistant.

Answer clearly and professionally.

Conversation History:
{conversation}

User Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    answer = response.text


    st.session_state.chat_history.append({
        "role": "assistant",
        "content": answer
    })

    return answer