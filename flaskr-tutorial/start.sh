#!/bin/bash

app="flaskr-tutorial"

echo "Building docker image '${app}'..."
docker build -t ${app} .

echo "Running docker container '${app}'..."
docker run -d -p 5000:5000 --name=${app} ${app}

docker ps -a