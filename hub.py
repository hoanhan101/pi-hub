"""
    hub.py - PiHub server
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/10/18
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from pprint import pprint
from time import ctime, time

import dummy_data
import helper
import sql

app = Flask(__name__)
CORS(app)

@app.route('/scan', methods=['GET'])
def scan():
    """
    Return all sensors with their locations.
    """
    response = helper.use_scan_schema(sql.get_sensor_and_location())
    return jsonify(response)

@app.route('/read/last_hour', methods=['GET'])
def read_last_hour():
    """
    Return all readings in the last hour.
    """
    response = helper.use_reading_schema(sql.get_readings_last_hour())
    return jsonify(response)

@app.route('/read/yesterday', methods=['GET'])
def read_yesterday():
    """
    Return all readings from yesterday.
    """
    response = helper.use_reading_schema(sql.get_readings_yesterday())
    return jsonify(response)

@app.route('/read/<int:sensor_id>', methods=['GET'])
def read_sensor_id(sensor_id):
    """
    Return all readings for a specific sensor id.
    """
    response = helper.use_reading_schema(sql.get_readings_from_sensor(sensor_id))
    return jsonify(response)

@app.route('/read/<int:sensor_id>/last_hour', methods=['GET'])
def read_sensor_id_last_hour(sensor_id):
    """
    Return all readings for a specific sensor id in the last hour.
    """
    response = helper.use_reading_schema(sql.get_readings_last_hour_by_id(sensor_id))
    return jsonify(response)

@app.route('/read/<int:sensor_id>/yesterday', methods=['GET'])
def read_sensor_id_yesterday(sensor_id):
    """
    Return all readings for a specific sensor id from yesterday.
    """
    response = helper.use_reading_schema(sql.get_readings_yesterday_by_id(sensor_id))
    return jsonify(response)

@app.route('/read/yesterday/max', methods=['GET'])
def read_yesterday_max():
    """
    Return maximum reading of all readings from yesterday.
    """
    response = helper.use_reading_schema(sql.get_max_reading_yesterday())
    return jsonify(response)

@app.route('/read/last_hour/max', methods=['GET'])
def read_last_hour_max():
    """
    Return maximum reading of all readings in the last hour.
    """
    response = helper.use_reading_schema(sql.get_max_reading_last_hour())
    return jsonify(response)

@app.route('/write', methods=['POST'])
def write():
    """
    Write to database endpoint.
    """
    # Get request data
    payload = request.get_json()

    # Validate POST data
    flag = helper.validate_post_data(payload)

    if flag is None:
        sql.insert_reading(payload.get('id'),
                           payload.get('location'),
                           payload.get('data').get('temperature').get('value'),
                           payload.get('data').get('temperature').get('unit'),
                           payload.get('data').get('humidity').get('value'))

        # Return back what the client POST with timestamp and status.
        response = {
            'id': payload.get('id'),
            'timestamp': ctime(time()),
            'error': None
        }

        pprint(response)
        return jsonify(response)

    else:
        # Return back what the client POST with timestamp and status.
        response = {
            'id': payload.get('id'),
            'timestamp': ctime(time()),
            'error': flag
        }

        pprint(response)
        return jsonify(response)

@app.route('/test', methods=['GET', 'POST'])
def test():
    """
    Test endpoint.
    """
    return jsonify(dummy_data.dummy_test)

@app.route('/config', methods=['GET'])
def config():
    """
    Return configurations.
    """
    return jsonify(dummy_data.dummy_config)

@app.route('/read/max', methods=['GET'])
def read_max():
    """
    Return maximum reading of all readings. 
    """
    return jsonify(dummy_data.dummy_read_max)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
