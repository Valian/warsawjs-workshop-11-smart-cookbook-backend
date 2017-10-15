FROM python:3.6

ENV PROJECT_DIR = '/srv'

WORKDIR $PROJECT_DIR

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY smart_cookbook/* .