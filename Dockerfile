# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /djPro
COPY requirements.txt /djPro/
RUN pip install -r requirements.txt
COPY . /djPro/

