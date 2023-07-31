# base image
FROM python:3.10

# making directory of app
WORKDIR /langchain-Document-Chat

# copy of requirements file
COPY requirements.txt .

# install pacakges
RUN pip install -r requirements.txt --default-timeout=100 future

# copying all files over
COPY . .

# exposing default port for streamlit
EXPOSE 8501

# command to launch app
CMD ["streamlit", "run", ".bin/app.py"]

