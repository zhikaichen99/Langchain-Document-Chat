# Langchain-Document-Chat

Developing a Streamlit application using `Langchain` and the `ChatGPT API` to enable users to ask questions on uploaded PDF documents.

Deploying the Streamlit application on an `AWS EC2` instance using `Docker`.

Medium article going over project is available here: https://medium.com/@zhikaichen1999/document-insights-document-qa-with-langchain-and-chatgpt-deployed-on-aws-ec2-1cb7dcf7495b

Demo of deployed Streamlit application available here: http://18.118.141.12:8501/


## Project Motivation

The motivation for this project was to gain experience using `Langchain` and `OpenAI`. Additionally, I wanted to gain experience deploying applications on Cloud services.

## Repository Structure and File Description

```markdown
├── bin                          # folder for main file
│   ├── app.py                   # code for Streamlit application
├── data                         # folder containing pdf documents
│   ├── sample-job-posting.pdf   # sample pdf document
├── notebooks                    # jupyter notebooks
│   ├── chat-document.ipynb      # main notebook     
├── src                          # folder containing functions
│   ├── conversation.py          # function to create conversation chain
│   ├── embedding.py             # function to load embedding model
│   ├── ingest.py                # function to extract text from pdf
│   ├── textchunks.py            # function to create chunks from text
│   └── vectorstore.py           # function to create vector database
├── Dockerfile                   # Dockerfile for application
├── requirements.txt             # libraries need for application
```

## Requirements
You will need an AWS account and an OPENAI_API_KEY if you want to follow along with the article.

## Installations
The packages and libraries required for this project are in the `requirements.txt` file.

## How to Interact With The Project
1. Clone the repository to your local machine using the following command:
```
git clone https://github.com/zhikaichen99/Langchain-Document-Chat.git
```
2. Navigate to repository
3. Install requirements by running:
```
pip install -r requirements.txt
```
4. Run the Streamlit application:
```
streamlit run .bin/app.py
```