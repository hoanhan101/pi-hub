#!/usr/bin/env bash
# start.sh - Configure database and start up server.
# Author: Hoanh An (hoanhan@bennington.edu)
# Date: 05/25/28

echo "Setup MySQL database"
python3 setup_mysql.py

echo "Sleep for 5 seconds"
sleep 5

echo "Run Flask"
/usr/local/bin/flask run --host=0.0.0.0
