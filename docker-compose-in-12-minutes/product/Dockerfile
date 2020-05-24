FROM python:3.8.2-slim-buster

RUN pip install --upgrade pip \
    && pip install pipenv

WORKDIR /app
COPY . /app
RUN pipenv install --deploy --ignore-pipfile
CMD ["pipenv", "run", "python", "/app/api.py"]