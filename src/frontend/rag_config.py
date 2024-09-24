# Create streamlit app

import streamlit as st

selected_model = None
temperature = None
submitted = None
max_tokens = None
selected_project_id = None
selected_project = None

def get_configs():
    with st.sidebar:
        with st.form("🗀 File Input", clear_on_submit=True):
            uploaded_files = st.file_uploader(
                "Upload local files:",
                type=["txt", "pdf", "docx", "csv", "jpg", "png", "jpeg", "py"],
                accept_multiple_files=True,
            )
            submitted = st.form_submit_button("Submit")
        if uploaded_files and submitted:
            st.session_state["uploaded_files"] = uploaded_files

        ex = st.expander("⚒ Conversation Configuration", expanded=True)
        with ex:
            last_submitted_embeddings = (len(st.session_state["projects"]) - 1) if st.session_state["projects"] else None
            selected_project = st.selectbox(
                "Select embeddings for query: ", 
                st.session_state["projects"], 
                on_change=change_id, 
                index=last_submitted_embeddings,
            )
        # select model and training parameters
        expander = st.expander("⚒ RAG Pipeline Configuration", expanded=True)
        with expander:
            st.subheader("Adjust RAG Parameters")
            max_tokens = st.number_input("Max Tokens", min_value=1, max_value=1024, value=512)
            temperature = st.slider("Temperature", min_value=0.01, max_value=2.0, value=0.0, step=0.01, format="%.1f")
        
        selected_model = st.selectbox("Select your preferred model: ", ["llama-3.1-70b-versatile","llama-3.1-8b-instant","mixtral-8x7b-32768"])


        vars = (selected_model, temperature, submitted, max_tokens, selected_project)
        return vars 

def change_id():
    selected_project_id = selected_project