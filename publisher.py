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
            Response data <dict>, status_code <int>
        """
        r = requests.post('{}/{}'.format(self.host, endpoint), json=payload)
        return r.json(), r.status_code
