#!/bin/bash

# Save current directory in OLD_DIR
OLD_DIR=$PWD
# Change directory to where the script is located
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd $DIR

cp $1 input.sqlite
docker build -t coffeebreak/pitchfork_crawler --build-arg pitchforkFolder=input.sqlite .
rm input.sqlite
docker volume create --name pitchfork_crawler_cache
docker run -it --name coffeebreak_pitchfork_crawler -v pitchfork_crawler_cache:/cache coffeebreak/pitchfork_crawler
rc=$?
docker cp coffeebreak_pitchfork_crawler:/app/output.json .
docker rm coffeebreak_pitchfork_crawler

# Go back to the former current directory
cd $OLD_DIR

echo "Exiting from container with status $rc"
exit $rc
