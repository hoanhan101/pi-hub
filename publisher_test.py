"""
    publisher_test.py - Test Publisher
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/20/2018
"""

from time import time, ctime
from publisher import Publisher

if __name__ == '__main__':
    worker = Publisher()

    assert 200 == worker.get('test')[1]

    empty_dict = {}
    assert 0 == worker.publish('test', empty_dict)[1]

    no_id = {
        'data': 'test'
    }
    assert 0 == worker.publish('test', no_id)[1]

    no_data = {
        'id': 1
    }
    assert 0 == worker.publish('test', no_data)[1]

    empty_data = {
        'id': 1,
        'data': {}
    }
    assert 0 == worker.publish('test', empty_data)[1]

    no_temp = {
        'id': 1,
        'data': {
            'humidity': {
                'value': 60.6,
                'unit': '%'
            }
        }
    }
    assert 0 == worker.publish('test', no_temp)[1]

    no_humd = {
        'id': 1,
        'data': {
            'temperature': {
                'value': 20.2,
                'unit': 'C'
            }
        }
    }
    assert 0 == worker.publish('test', no_humd)[1]

    non_float_temp_value = {
        'id': 1,
        'data': {
            'temperature': {
                'value': 20,
                'unit': 'C'
            },
            'humidity': {
                'value': 60.6,
                'unit': '%'
            }
        }
    }
    assert 0 == worker.publish('test', non_float_temp_value)[1]

    non_float_humd_value = {
        'id': 1,
        'data': {
            'temperature': {
                'value': 20.0,
                'unit': 'C'
            },
            'humidity': {
                'value': 60,
                'unit': '%'
            }
        }
    }
    assert 0 == worker.publish('test', non_float_humd_value)[1]

    non_str_temp_unit = {
        'id': 1,
        'data': {
            'temperature': {
                'value': 20.0,
                'unit': 20.0
            },
            'humidity': {
                'value': 60.6,
                'unit': '%'
            }
        }
    }
    assert 0 == worker.publish('test', non_str_temp_unit)[1]

    non_str_humd_unit = {
        'id': 1,
        'data': {
            'temperature': {
                'value': 20.0,
                'unit': 'C'
            },
            'humidity': {
                'value': 60.6,
                'unit': 60.6
            }
        }
    }
    assert 0 == worker.publish('test', non_str_humd_unit)[1]

    good_payload = {
        'id': 1,
        'data': {
            'temperature': {
                'value': 20.0,
                'unit': 'C'
            },
            'humidity': {
                'value': 60.6,
                'unit': '%'
            }
        }
    }
    assert 200 == worker.publish('test', good_payload)[1]
