FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.tst

CMD [ "python3","app.py"]
