FROM python:3.7-slim-buster

LABEL maintainer="Johannes Giorgis"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "flask", "run", "--host=0.0.0.0"]