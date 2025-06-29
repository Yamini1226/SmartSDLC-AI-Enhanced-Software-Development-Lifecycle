import streamlit as st
import requests

st.title("SmartSDLC Toolkit")

st.header("User Stories Generator")
pdf_text = st.text_area("Paste PDF text here:", key="pdf_text")
if st.button("Generate User Stories"):
    response = requests.post(
        "http://localhost:8000/ai/generate-user-stories",
        params={"pdf_text": pdf_text}
    )
    if response.ok:
        st.write(response.json())
    else:
        st.error("Error from backend (User Stories)")

import streamlit as st
import requests

st.header("AI Code Generator")
task_description = st.text_input("Describe the code you want to generate:", key="codegen_input")
if st.button("Generate Code"):
    if task_description:
        response = requests.post(
            "http://localhost:8000/ai/generate-code",
            params={"task_description": task_description}
        )
        if response.ok:
            code = response.json().get("code", "")
            st.code(code, language="python")
        else:
            st.error("Error from backend (Code Generator)")

st.header("Bug Resolver")
buggy_code = st.text_area("Paste buggy code here:", key="buggy_code")
if st.button("Fix Bug"):
    response = requests.post(
        "http://localhost:8000/ai/fix-bug",
        params={"code_snippet": buggy_code}
    )
    if response.ok:
        st.code(response.json().get("fixed_code", ""), language="python")
    else:
        st.error("Error from backend (Bug Resolver)")

st.header("Test Case Generator")
test_input = st.text_area("Paste code or requirement for test case generation:", key="test_input")
if st.button("Generate Test Cases"):
    response = requests.post(
        "http://localhost:8000/ai/generate-test-cases",
        params={"code_or_requirement": test_input}
    )
    if response.ok:
        test_cases = response.json().get("test_cases", [])
        for tc in test_cases:
            st.code(tc, language="python")
    else:
        st.error("Error from backend (Test Case Generator)")
st.header("Code Summarizer")
code_to_summarize = st.text_area("Paste code to summarize:", key="code_to_summarize")
if st.button("Summarize Code"):
    response = requests.post(
        "http://localhost:8000/ai/summarize-code",
        params={"code_snippet": code_to_summarize}
    )
    if response.ok:
        st.success(response.json().get("summary", "No summary generated."))
    else:
        st.error("Error from backend (Code Summarizer)")
st.header("AI Chatbot Assistant")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_message = st.text_input("Ask the AI Assistant:", key="chat_input")
if st.button("Send"):
    if user_message:
        response = requests.post(
            "http://localhost:8000/ai/chatbot",
            params={"message": user_message}
        )
        if response.ok:
            ai_response = response.json().get("response", "")
            st.session_state.chat_history.append(("You", user_message))
            st.session_state.chat_history.append(("AI", ai_response))
        else:
            st.error("Error from backend (Chatbot)")

for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")