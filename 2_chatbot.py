from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-120b")

st.title("My Buddy - My Personal Assistant")
st.markdown("My personal chatbot built with the Groq LLM and LangChain")

query = st.chat_input("Ask Anything...")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]
    st.chat_message(role).markdown(content)

if query:

    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    st.chat_message("user").markdown(query)

    res = llm.invoke(st.session_state.messages)

    st.chat_message("assistant").markdown(res.content)

    st.session_state.messages.append(
        {"role": "assistant", "content": res.content}
    )