"""
    setup_mysql.py - Script to setup MySQL properly
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/25/18
"""

import mysql.connector
from mysql.connector import errorcode

import config

DB_NAME = config.DATABASE

TABLES = {}
TABLES['readings'] = (
        "CREATE TABLE `readings` ("
        "  `sensor_id` int(11) NOT NULL,"
        "  `location` int(11) NOT NULL,"
        "  `temp` double(11, 5) NOT NULL,"
        "  `temp_degree` char(1) NOT NULL,"
        "  `humidity` double(11, 5) NOT NULL,"
        "  `timestamp` datetime NOT NULL ) ENGINE=MyISAM DEFAULT CHARSET=latin1;"
        )

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

if __name__ == '__main__':
    cnx = mysql.connector.connect(host=config.HOST, port=config.PORT,
                                  user=config.USER, password=config.PASSWORD)
    cursor = cnx.cursor()

    try:
        cnx.database = DB_NAME  
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

    for name, ddl in TABLES.items():
        try:
            print("Creating table {}: ".format(name), end='')
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()
