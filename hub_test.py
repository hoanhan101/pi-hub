"""
    hub_test.py - Test hub endpoints
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/23/18
"""

import requests

import config
import helper

def test_get(endpoint, url=config.URL):
    r = requests.get('{}/{}'.format(url, endpoint))
    print('/{}\t{}'.format(endpoint, r.status_code))

if __name__ == '__main__':
    # GET
    test_get('test')
    test_get('config')
    test_get('scan')
    test_get('read/last_hour')
    test_get('read/yesterday')
    test_get('read/1')
    test_get('read/1/last_hour')
    test_get('read/1/yesterday')
    test_get('read/max')
    test_get('read/yesterday/max')

    # POST
    helper.post(1, 2, 20.2, 60.6)
