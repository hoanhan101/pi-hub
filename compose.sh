#!/usr/bin/env bash
# compose.sh - Link mysql-server container to pi-hub container.
# Author: Hoanh An (hoanhan@bennington.edu)
# Data: 05/25/18
# Note: A better way would be using docker compose. However, this allows more freedom.

echo "Run mysql-server"
docker run --name=mysql1 -e MYSQL_ALLOW_EMPTY_PASSWORD=true -e MYSQL_ROOT_HOST=172.17.0.3 -d mysql/mysql-server:latest

echo "Sleep for 5 seconds"
sleep 5

echo "Build pi-hub"
docker build -t pi-hub .

echo "Sleep for 5 seconds"
sleep 5

echo "Link mysql-server to pi-hub"
docker run --name sql-hub -p 5000:5000 --link mysql1:mysql -d pi-hub

echo "Attach to log"
docker logs -f sql-hub
