"""
    hub.py - PiHub server
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/10/18
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

from dummy_data import *
from sql_functions import *

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET', 'POST'])
def test():
    """
    Test endpoint.
    """
    return jsonify(dummy_test)

@app.route('/config', methods=['GET'])
def config():
    """
    Return configurations.
    """
    return jsonify(dummy_config)

@app.route('/scan', methods=['GET'])
def scan():
    """
    Return all sensors with their locations.
    """
    return jsonify(dummy_scan)

@app.route('/read/last_hour', methods=['GET'])
def read_last_hour():
    """
    Return all readings in the last hour.
    """
    # Get raw data from database read.
    raw_data = get_readings_last_hour()

    # Prepare a list of reponse object
    response = []
    for item in raw_data:
        scheme = {
            'id': item[0],
            'timestamp': item[4],
            'data': {
                'temperature': {
                    'value': item[1],
                    'unit': item[2]
                },
                'humidity': {
                    'value': item[3],
                    'unit': '%'
                }
            }
        }

        response.append(scheme)

    return jsonify(response)

@app.route('/read/yesterday', methods=['GET'])
def read_yesterday():
    """
    Return all readings from yesterday.
    """
    return jsonify(dummy_read)

@app.route('/read/<int:sensor_id>', methods=['GET'])
def read_sensor_id(sensor_id):
    """
    Return all readings for a specific sensor id.
    """
    dummy_sensor_read['id'] = sensor_id
    return jsonify(dummy_sensor_read)

@app.route('/read/<int:sensor_id>/last_hour', methods=['GET'])
def read_sensor_id_last_hour(sensor_id):
    """
    Return all readings for a specific sensor id in the last hour.
    """
    dummy_sensor_read['id'] = sensor_id
    return jsonify(dummy_sensor_read)

@app.route('/read/<int:sensor_id>/yesterday', methods=['GET'])
def read_sensor_id_yesterday(sensor_id):
    """
    Return all readings for a specific sensor id from yesterday.
    """
    dummy_sensor_read['id'] = sensor_id
    return jsonify(dummy_sensor_read)

@app.route('/read/max', methods=['GET'])
def read_max():
    """
    Return maximum reading of all readings. 
    """
    return jsonify(dummy_read_max)

@app.route('/read/yesterday/max', methods=['GET'])
def read_yesterday_max():
    """
    Return maximum reading of all readings from yesterday.
    """
    return jsonify(dummy_read_max)

@app.route('/write', methods=['POST'])
def write():
    """
    Write to database endpoint.
    """
    # Return back what the client POST with timestamp and status.
    response = {
        'timestamp': ctime(time()),
        'status': 'ok',
        'data': request.get_json()
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
