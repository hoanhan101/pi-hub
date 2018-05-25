#!/usr/bin/env bash

python3 start_mysql.py
sleep 5
/usr/local/bin/flask run --host=0.0.0.0
