import streamlit as st
import os
import sys
from dotenv import load_dotenv, find_dotenv

current_path = os.path.dirname(os.path.abspath(__file__))
parent_folder_path = os.path.abspath(os.path.join(current_path, os.pardir))
sys.path.append(parent_folder_path)

from src.ingest import pdf_to_text
from src.textchunks import create_text_chunks
from src.embedding import embedder
from src.vectorstore import create_vectorstore
from src.conversation import create_conversation_chain

# Load environment variables
load_dotenv(find_dotenv())

os.environ["OPENAI_API_KEY"] = "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"


# Set app title and page config
st.set_page_config(page_title="🤗 Langchain Document Chat")
st.sidebar.title('🤗 Langchain Document Chat')

def process_pdf_docs(pdf_docs, model_type):
    # Extract text from pdf documents
    text = pdf_to_text(pdf_docs)
    # Create text chunks
    text_chunks = create_text_chunks(text)
    # Load embedding
    embedding = embedder(model_type)
    # Create vector store
    vectorstore = create_vectorstore(text_chunks, embedding)
    # Create conversation chain
    return create_conversation_chain(model_type, vectorstore)

def main():
    # Initialize session state variables
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # Sidebar widgets
    model_type = st.sidebar.selectbox("Select Model Type", ["Open AI"])
    pdf_docs = st.sidebar.file_uploader("Upload PDF file and click Process", accept_multiple_files=True)

    # Process PDF documents and create conversation chain on button click
    if st.sidebar.button("Process"):
        with st.spinner("Processing"):
            st.session_state.conversation = process_pdf_docs(pdf_docs, model_type)

    # Display chat interface if documents have been processed
    if pdf_docs:
        prompt = st.chat_input("How can I help you?")
        if prompt:
            response = st.session_state.conversation({"question": prompt})
            st.session_state.chat_history = response["chat_history"]

            for i, message in enumerate(st.session_state.chat_history):
                with st.chat_message("user" if i % 2 == 0 else "assistant"):
                    st.markdown(message.content)

if __name__ == "__main__":
    main()
