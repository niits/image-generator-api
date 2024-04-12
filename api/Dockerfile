FROM python:3.11-slim

COPY ./requirements.txt /tmp/

RUN python3 -m pip install -U pip \
      && pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /

COPY ./app /app

EXPOSE 3000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]

