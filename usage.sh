#!/bin/sh

# Get the container ID
CONTAINER=$(docker inspect --format="{{.Id}}" nginx-local)

# while the container is running, output the stats.
while [ "$(docker inspect -f {{.State.Running}} $CONTAINER 2>/dev/null)" = "true" ]; do
    docker stats $container --no-stream
    sleep 5
done