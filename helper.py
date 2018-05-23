"""
    helper.py - Helper functions
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/23/18
"""

import json
import requests

from pprint import pprint

from config import URL


def use_scan_schema(data):
    """
    Convert data to a custom scan schema.
    The output will have this format:
        {
            'sensors': [
                {
                    'id': <int>,
                    'location': <int>
                }
                ...
            ]
        }

    Params:
        data <list>: List of database object.

    Return:
        Data in dictionary format.
    """
    result = {}
    sensors = []

    for item in data:
        scheme = {
            'id': item[0],
            'location': item[1]
        }

        sensors.append(scheme)

    result['sensors'] = sensors
    return result

def use_reading_schema(data):
    """
    Convert data to a custom reading schema.
    The output will have this format:
        [
            {
                'id': <int>,
                'timestamp': <unix_time>.
                'data': {
                    'temperature': {
                        'value': <float>,
                        'unit': <string>
                    },
                    'humidity': {
                        'value': <float>,
                        'unit': <string>
                    }
                }
            },
            ...
        ]

    Params:
        data <list>: List of database object.
    
    Return:
        List of dictionary.
    """
    result = []

    for item in data:
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

        result.append(scheme)

    return result

def post(sensor_id, location, temp, humd):
    """
    Publish a sensor reading to the server.

    Params:
        sensor_id <int>: Sensor ID
        location <int>: Location number
        temp <float>: Temperature value
        humd <float>: Humidity value

    Return:
        None
    """
    # Construct a payload
    payload = {
        'id': sensor_id,
        'location': location,
        'data': {
            'temperature': {
                'value': temp,
                'unit': 'C'
            },
            'humidity': {
                'value': humd,
                'unit': '%'
            }
        }
    }
    
    # Send a request
    r = requests.post('{}/{}'.format(URL, 'write'), json=payload)

    # Print out returned message.
    pprint(r.json())

def validate_post_data(data):
    """
    Validate POST data.

    Params:
        data <dict>: POST data

    Return:
        None if data is valid. Otherwise, error message in string format.
    """

    id = data.get('id')
    location = data.get('location')
    temp = data.get('data').get('temperature').get('value')
    temp_unit = data.get('data').get('temperature').get('unit')
    humd = data.get('data').get('humidity').get('value')

    if not isinstance(id, int):
        return 'ID must be an integer'

    if not isinstance(location, int):
        return 'Location must be an integer'

    if not isinstance(temp, float):
        return 'Temperature value must be a float'

    if not isinstance(humd, float):
        return 'Humidity value must be a float'

    if not isinstance(temp_unit, str):
        return 'Temperature unit must be a string'

    return None
