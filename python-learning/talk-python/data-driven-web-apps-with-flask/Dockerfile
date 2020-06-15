#FROM python:3.6.10-slim-buster
FROM ubuntu:18.04

# Build
#$ docker build --rm --no-cache -t family-tree-api:1.0 .

#RUN apt update && apt upgrade -y \
#    && apt install git curl -y \
#    && pip install --upgrade pip \
#    && pip install pipenv

RUN apt update && apt upgrade -y \
    && apt install vim git curl -y

ENV FTA=/pypi_org
WORKDIR ${FTA}

COPY Pipfile* ./

#RUN pipenv install --deploy --ignore-pipfile
COPY . .

#CMD ["pipenv", "run", "python", "manage.py"]
# ensure docker image keeps running
CMD tail -f /dev/null
