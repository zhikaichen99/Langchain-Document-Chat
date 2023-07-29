from langchain.embeddings import OpenAiEmbeddings
from langchain.vectorstores import FAISS

def create_vectorstore(text):
    """
    This function embeds the text from the document and stores in a vectorstore

    Inputs:
        text - extracted text from document
    Outputs: 
        vectorstore - vector store containing the embedded text
    """
    
    # Load OpenAI embedding model
    embeddings = OpenAiEmbeddings()
    # create vectorstore and store embedded text
    vectorstore = FAISS.from_texts(text = text, embedding = embeddings)
    return vectorstore