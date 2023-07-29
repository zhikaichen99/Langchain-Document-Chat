from langchain.vectorstores import FAISS

def create_vectorstore_openai(text, embedding_model):
    """
    This function embeds the text from the document and stores in a vectorstore

    Inputs:
        text - extracted text from document
        embedding_model - embedding model
    Outputs: 
        vectorstore - vector store containing the embedded text
    """
    # create vectorstore and store embedded text
    vectorstore = FAISS.from_texts(text = text, embedding = embedding_model)
    return vectorstore