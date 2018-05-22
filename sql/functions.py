
#!usr/bin/env python3
import mysql.connector
import datetime
import json


#set variables. note that the host can change if the ip adress the mysql container runs in changes.
host = "localhost"
user = "root"
psswd = "sensorworkshop"
database = "sensor_workshop"

# following email, will do:
#- get all temperature readings in the last hour
#- get all temperature readings in yesterday
#- get all temperature readings from sensor x
#- get temperature readings from sensor x in the last hour
#- get temperature readings from sensor x in yesterday

# Worth mentioning: SELECT statements return the full row and not just one column. Can edit if needed.

from mysql.connector import errorcode
try:
  cnx = mysql.connector.connect(host, user, psswd, database)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()




def connect():
    link = mysql.connector.connect(user = user, password= psswd, host = host, database = database)
    return link;

def insert_reading(id, loc, temp, d, hum):
    link = connect()
    cursor = link.cursor()
    q = "INSERT INTO readings (sensor_id, location, temp, temp_degree, humidity, timestamp) VALUES (%s, %s, %s, %s, %s, NOW())"
    cursor.execute(q, (id, loc, temp, d, hum))


def get_readings_from_sensor(id):
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE sensor_id="+str(id)
    cursor.execute(q)
    info = cursor.fetchall()
    return json.dumps(info);


def get_readings_yesterday():
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE DATEDIFF(CURDATE(), DATE(timestamp))=1"
    cursor.execute(q)
    info = cursor.fetchall()
    return json.dumps(info)


def get_readings_last_hour():
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE TIME_TO_SEC(TIMEDIFF(NOW(), timestamp)) BETWEEN 0 AND 3600"
    cursor.execute(q)
    info = cursor.fetchall()
    return json.dumps(info);



