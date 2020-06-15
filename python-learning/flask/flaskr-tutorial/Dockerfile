# Alpine base image that contains python 3.7
FROM python:3.7-alpine

# Label details
LABEL maintainer="Johannes Giorgis"
LABEL build_date="2019-10-03"

# define the directory to work in
WORKDIR /app

# copy the requirements.txt file to the work directory
COPY ./requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

# Copy source code
COPY . /app

# Running Command or Entry Point
CMD [ "flask", "run", "--host=0.0.0.0"]