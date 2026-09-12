#loading the environmentall varibales
from dotenv import load_dotenv

load_dotenv()
#import streamlit
import streamlit as st

#create llm

from langchain_groq import ChatGroq
llm =ChatGroq(model ="openai/gpt-oss-120b")
st.title("My Budyy -My Personal Assistant")
st.markdown("My personal chatbot built with the groq LLM and langchain")
query =st.chat_input("Ask Anything..")
if "messages" not in st.session_state:
    st.session_state.messages=[]   #storing he messages in the session state




for msg in st.session_state.messages:
    role=msg["role"]
    content=msg["content"]
    st.chat_message(role).markdown(content)
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)

    res = llm.invoke(query)
    st.chat_message("AI").markdown(res.content)
    st.session_state.messages.append({"role":"Ai","content":res.content})




