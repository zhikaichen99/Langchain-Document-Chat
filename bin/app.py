import streamlit as st
import sys
import os
from dotenv import load_dotenv, find_dotenv


current_path = os.path.dirname(os.path.abspath(__file__))
parent_folder_path = os.path.abspath(os.path.join(current_path, os.pardir))
sys.path.append(parent_folder_path)


from src.ingest import pdf_to_text
from src.textchunks import create_text_chunks
from src.embedding import embedder
from src.vectorstore import create_vectorstore
from src.conversation import create_conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html = True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html = True)
    


_ = load_dotenv(find_dotenv())


# App title
st.set_page_config(page_title="🤗💬 HugChat")

if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = None


# Hugging Face Credentials
with st.sidebar:
    st.title('🤗💬 HugChat')

    model_type = st.selectbox("Select Model Type", ["Open AI", "Hugging Face"])

    pdf_docs = st.file_uploader(
        "Upload PDF File and Hit Process", accept_multiple_files = True
    )
    if st.button("Process"):
        with st.spinner("Processing"):
            # extract text from pdf document
            text = pdf_to_text(pdf_docs)
            # create text chunks
            text_chunks = create_text_chunks(text)
            # load embedding
            embedding = embedder(model_type)
            # creat vector store
            vectorstore = create_vectorstore(text_chunks, embedding)
            # create conversation chain
            st.session_state.conversation = create_conversation_chain(model_type, vectorstore)

if pdf_docs:
    if prompt := st.chat_input("How can I help you?"):
        response = st.session_state.conversation({"question": prompt})
        st.session_state.chat_history = response["chat_history"]

        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                with st.chat_message("user"):
                    st.markdown(message.content)
            else:
                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = ""
                    full_response += message.content
                    message_placeholder.markdown(full_response)
        

