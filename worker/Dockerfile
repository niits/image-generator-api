# syntax=docker/dockerfile:1

FROM python:3.11-slim

COPY requirements.txt /tmp/

RUN python -m pip install pip -U && pip install -r /tmp/requirements.txt --no-cache-dir

COPY ./app /app/

WORKDIR /

CMD celery -A app.tasks worker --loglevel=info