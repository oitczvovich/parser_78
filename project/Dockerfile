FROM python:3.11-slim

WORKDIR /parser/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ../requirements.txt ./requirements.txt

RUN pip3 install -r /parser/requirements.txt --no-cache-dir

COPY . /parser
