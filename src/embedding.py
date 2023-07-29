from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS

def openai_embedder():
    # load OpenAI embedding model
    embeddings = OpenAIEmbeddings()
    return embeddings

def huggingface_embedder():
    # load huggingface embedding model
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    return embeddings
