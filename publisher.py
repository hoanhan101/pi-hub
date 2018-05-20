"""
    publisher.py - Publisher pushs sensor reading to PiHub 
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/10/18
"""

import json
import requests

from config import url

class Publisher():
    def __init__(self, host=url):
        """
        Initialize a Publisher object.

        Params:
            host <str>: Target hostname

        Return:
            None
        """
        self.host = host

    def get(self, endpoint):
        """
        Call GET for a specific endpoint.

        Params:
            endpoint <str>: Endpoint

        Return:
            Response data <dict>, status_code <int>
        """
        r = requests.get('{}/{}'.format(self.host, endpoint))
        return r.json(), r.status_code

    def publish(self, endpoint, payload):
        """
        Publish sensors reading to a specific endpoint.

        Params:
            endpoint <str>: Endpoint
            payload <str>: Data payload

        Return:
            Response data <dict>, status_code <int> if succeed. None and 0 if fail.
        """
        # Validate POST data
        if payload.get('id') is None:
            print('There is no id field')
            return None, 0

        if payload.get('data') is None:
            print('There is no data field')
            return None, 0

        data = payload.get('data')

        if data.get('temperature') is None:
            print('There is no temperature field')
            return None, 0

        if data.get('humidity') is None:
            print('There is no humidity field')
            return None, 0

        if not isinstance(data.get('temperature').get('value'), float):
            print('Temperature value must be float')
            return None, 0
    
        if not isinstance(data.get('temperature').get('unit'), str):
            print('Temperature unit must be string')
            return None, 0

        if not isinstance(data.get('humidity').get('value'), float):
            print('Humidity value must be float')
            return None, 0

        if not isinstance(data.get('humidity').get('unit'), str):
            print('Humidity unit must be string')
            return None, 0

        r = requests.post('{}/{}'.format(self.host, endpoint), json=payload)
        return r.json(), r.status_code
