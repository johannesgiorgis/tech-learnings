#!/bin/bash

app="flaskr-tutorial"

echo "Stopping docker container '${app}'..."
docker stop ${app}

echo "Removing docker container '${app}'..."
docker rm ${app}

docker ps -a