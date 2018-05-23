
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
#- get all sensor ids with their locations
#- get all readings
#- get all reading for a given sensor id in the last hour
#- get all reading for a given sensor id from yesterday
#- get max reading in the last hour
#- get max reading from yesterday
#- clean up the table (just for quick testing)

# Due to some weird error with PDO, parameters will not be passed through placeholders at times.

# Worth mentioning: SELECT statements return the full row and not just one column. Can edit if needed.




def connect():
    link = mysql.connector.connect(user = user, password= psswd, host = host, database = database)
    return link;


#Insert reading
def insert_reading(id, loc, temp, d, hum):
    link = connect()
    cursor = link.cursor()
    q = "INSERT INTO readings (sensor_id, location, temp, temp_degree, humidity, timestamp) VALUES (%s, %s, %s, %s, %s, NOW())"
    cursor.execute(q, (id, loc, temp, d, hum))
    link.close()

#Gets all readings from sensor
def get_readings_from_sensor(id):
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE sensor_id="+str(id)
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info


#Gets all readings from the day before
def get_readings_yesterday():
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE DATEDIFF(CURDATE(), DATE(timestamp))=1"
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info


#Gets all the readings from the last hour
def get_readings_last_hour():
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE TIME_TO_SEC(TIMEDIFF(NOW(), timestamp)) BETWEEN 0 AND 3600"
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info


#Gets all readings
def get_all_readings():
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings "
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info

#Gets all readings from the day before by sensor id
def get_readings_yesterday_by_id(id):
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE DATEDIFF(CURDATE(), DATE(timestamp))=1 AND sensor_id="+id
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info


#Gets all the readings from the last hour by sensor id
def get_readings_last_hour_by_id(id):
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE (TIME_TO_SEC(TIMEDIFF(NOW(), timestamp)) BETWEEN 0 AND 3600) AND sensor_id="+id
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info


#Gets max reading from the day before
def get_max_reading_yesterday():
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE DATEDIFF(CURDATE(), DATE(timestamp))=1 AND temp=(SELECT MAX(temp) from readings)"
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info


#Gets max readings from the last hour
def get_max_reading_last_hour():
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE (TIME_TO_SEC(TIMEDIFF(NOW(), timestamp)) BETWEEN 0 AND 3600) AND temp=(SELECT MAX(temp) FROM readings)"
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info

#Clear table
def clear_table():
    link = connect()
    cursor = link.cursor()
    q = "TRUNCATE readings"
    cursor.execute(q)
    link.close()

#Get all location and sensors
def get_sensor_and_location():
    link = connect()
    cursor = link.cursor()
    q = "SELECT DISTINCT sensor_id, location FROM readings ORDER BY location"
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info
