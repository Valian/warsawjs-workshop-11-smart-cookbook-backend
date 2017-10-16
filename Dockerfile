FROM python:3.6

ENV PROJECT_DIR /srv

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . $PROJECT_DIR

WORKDIR $PROJECT_DIR/smart_cookbook