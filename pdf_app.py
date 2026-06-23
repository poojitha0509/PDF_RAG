import streamlit as st

from agent_backend import (
    process_pdf,
    search_pdf
)

st.set_page_config(
    page_title="PDF Chatbot"
)

st.title("📄 PDF Chatbot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    if st.button("Process PDF"):

        with st.spinner("Processing PDF..."):

            msg = process_pdf(uploaded_file)

        st.success(msg)

question = st.text_input(
    "Ask a question"
)

if st.button("Search"):

    docs = search_pdf(question)

    st.subheader("Results")

    for doc in docs:
        st.write(doc.page_content)
        st.divider()