#!/bin/bash
# import.sh: Import database to mysql server
# Author: Hoanh An (hoanhan@bennington.edu)
# Date: 05/23/18

mysql -u root -e "create database sensor_workshop";
mysql -u root -p sensor_workshop < schema.sql
