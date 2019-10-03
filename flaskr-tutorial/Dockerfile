FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev python3-venv locales && \
    rm -rf /var/lib/apt/lists/* && locale-gen "en_CA.UTF-8"

# Set the locale
ENV LANG en_CA.UTF-8
# ENV LC_ALL en_CA.UTF-8

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 --version
RUN which pip3
RUN pip3 --version
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

#ENTRYPOINT [ "python3" ]

CMD [ "flask", "run", "--host=0.0.0.0"]


#CMD tail -f /dev/null