import streamlit as st
from agent_core.agent_runner import run_agent

st.title("AI Solutions Architect")
query = st.text_input("Enter your question")
if query:
    st.write(run_agent(query))