"""
    sql_functions.py - SQL functions
    Based on sql/functions.py written by Paulina Valdivieso (paulinavaldivieso@bennington.edu)
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/22/18
"""

import mysql.connector
import datetime
import json

# Configurations
host = 'localhost'
user = 'root'
psswd = ''
database = 'sensor_workshop'

def connect():
    """
    Connect to database.

    Params:
        None

    Return:
        A connection link.
    """
    link = mysql.connector.connect(host=host, user=user, password=psswd, database=database)
    return link

def insert_reading(id, loc, temp, d, hum):
    """
    Insert sensor reading to the table.

    Params:
        id <int>: Sensor ID
        loc <int>: Sensor's location
        temp <float>: Temperature value
        d <str>: Temperature degree
        hum <float>: Temperature value

    Return:
        None
    """
    link = connect()
    cursor = link.cursor()
    q = "INSERT INTO readings (sensor_id, location, temp, temp_degree, humidity, timestamp) VALUES (%s, %s, %s, %s, %s, NOW())"
    cursor.execute(q, (id, loc, temp, d, hum))
    link.close()

def get_all_readings():
    """
    Get all readings from the table.

    Params:
        None

    Return:
        Data in list.
    """
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings"
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info

def get_readings_yesterday():
    """
    Get all readings from yesterday

    Params:
        None

    Return:
        Data in list.
    """
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE DATEDIFF(CURDATE(), DATE(timestamp))=1"
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info

def get_readings_last_hour():
    """
    Get all readings from the last hour.

    Params:
        None

    Return:
        Data in list.
    """
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE TIME_TO_SEC(TIMEDIFF(NOW(), timestamp)) BETWEEN 0 AND 3600"
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info

def get_readings_from_sensor(id):
    """
    Get all readings for a specific sensor.

    Params:
        id <int>: Sensor ID

    Return:
        Data in list.
    """
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE sensor_id="+str(id)
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info

def get_readings_yesterday_by_id(id):
    """
    Get all readings from yesterday for a specific sensor.

    Params:
        id <int>: Sensor ID

    Return:
        Data in list.
    """
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE DATEDIFF(CURDATE(), DATE(timestamp))=1 AND sensor_id="+str(id)
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info

def get_readings_last_hour_by_id(id):
    """
    Get all readings in the last hour for a specific sensor.

    Params:
        id <int>: Sensor ID

    Return:
        Data in list.
    """
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE (TIME_TO_SEC(TIMEDIFF(NOW(), timestamp)) BETWEEN 0 AND 3600) AND sensor_id="+str(id)
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info

def get_max_reading_yesterday():
    """
    Get maximum reading from yesterday.

    Params:
        None

    Return:
        Data in list.
    """
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE DATEDIFF(CURDATE(), DATE(timestamp))=1 AND temp=(SELECT MAX(temp) from readings)"
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info

def get_max_reading_last_hour():
    """
    Get maximum reading in the last hour.

    Params:
        None

    Return:
        Data in list.
    """
    link = connect()
    cursor = link.cursor()
    q = "SELECT sensor_id,temp,temp_degree,humidity, CAST(timestamp AS CHAR(30)) FROM readings WHERE (TIME_TO_SEC(TIMEDIFF(NOW(), timestamp)) BETWEEN 0 AND 3600) AND temp=(SELECT MAX(temp) FROM readings)"
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info

def clear_table():
    """
    Quick way to clean up the table

    Params:
        None

    Return:
        None
    """
    link = connect()
    cursor = link.cursor()
    q = "TRUNCATE TABLE readings;"
    cursor.execute(q)
    link.close()

def get_sensor_and_location():
    """
    Get all sensors with their locations.

    Params:
        None

    Return:
        Data in list.
    """
    link = connect()
    cursor = link.cursor()
    q = "SELECT DISTINCT sensor_id, location FROM readings ORDER BY location"
    cursor.execute(q)
    info = cursor.fetchall()
    link.close()
    return info
