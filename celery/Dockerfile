FROM python:3.8

WORKDIR /usr/src/app

RUN pip install celery[redis]==5.2.7

COPY app.py .
COPY celery_config.py .