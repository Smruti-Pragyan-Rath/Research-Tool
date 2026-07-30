import streamlit as st
from rag import process_urls, generate_answer

st.set_page_config(page_title="News Research Tool")

st.title("Research Tool")

if "processed" not in st.session_state:
    st.session_state.processed = False

st.sidebar.title("Article URLs")

urls = []

for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")

    if url.strip():
        urls.append(url)

if st.sidebar.button("Process URLs"):

    if len(urls) == 0:
        st.sidebar.error("Please enter at least one URL.")

    else:

        with st.spinner("Processing URLs..."):

            process_urls(urls)

        st.session_state.processed = True

        st.sidebar.success("Knowledge Base Ready!")

st.header("Ask Questions")

question = st.text_input("Question")

if st.button("Ask"):

    if not st.session_state.processed:
        st.warning("Please process URLs first.")

    elif question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            answer, sources = generate_answer(question)

        st.subheader("Answer")

        st.write(answer)

        if sources:
            st.subheader("Sources")
            st.write(sources)