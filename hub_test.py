"""
    hub_test.py - Test hub endpoints
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/23/18
"""

import requests

from time import ctime, time

from pprint import pprint

import config
import helper

def test_get(endpoint, url=config.URL):
    """
    Test GET endpoint.

    Params:
        endpoint <str>: Endpoint
        url <str>: Target URL

    Return:
        None
    """
    r = requests.get('{}/{}'.format(url, endpoint))
    print('\033[92m/{}\t{}\033[0m'.format(endpoint, r.status_code))

    if r.status_code == 429:
        response = {
            'error': '429 Too Many Requests',
            'timestamp': ctime(time())
        }
        pprint(response)
    if r.status_code == 403:
        response = {
            'error': '403 Forbidden',
            'timestamp': ctime(time())
        }
        pprint(response)
    else:
        pprint(r.json())

    return r.status_code

if __name__ == '__main__':
    # GET
    assert 200 == test_get('test')
    assert 200 == test_get('config')
    assert 200 == test_get('scan')
    assert 200 == test_get('read/all')
    assert 200 == test_get('read/max')
    assert 200 == test_get('read/last_hour')
    assert 200 == test_get('read/last_hour/max')
    assert 200 == test_get('read/yesterday')
    assert 200 == test_get('read/yesterday/max')
    assert 200 == test_get('read/1')
    assert 200 == test_get('read/1/last_hour')
    assert 200 == test_get('read/1/yesterday')

    # POST
    assert 200 == helper.post(1, 'A1', 20.2, 60.6)
    assert 200 == helper.post(1, 'A1000000000000', 20.2, 60.6)
    assert 200 == helper.post(1.0, 'A10', 20.2, 60.6)
    assert 200 == helper.post(1, 'A10', 20, 60.6)
    assert 200 == helper.post(1, 'A10', 20.2, 60)

    # Clean up
    assert 403 == test_get('clean')
    assert 200 == test_get('read/all')
