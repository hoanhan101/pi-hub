"""
    dummy_data.py - Just some dummy data to test against endpoints
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/15/2018
"""

from time import time, ctime

dummy_test = {
    'status': 'ok',
    'timestamp': ctime(time())
}

dummy_config = {
    'debug': True,
    'pretty_json': True
}

dummy_scan = {
    'sensors': [
        {
            'id': 1,
            'location': '01'
        },
        {
            'id': 2,
            'location': '02'
        },
        {
            'id': 3,
            'location': '03'
        }
    ]
}

dummy_read = [
    {
        'id': 1,
        'timestamp': ctime(time()),
        'data': {
            'humidity': {
                'value': 70.7,
                'unit': '%'
            },
            'temperature': {
                'value': 20.2,
                'unit': 'C'
            }
        }
    },
    {
        'id': 2,
        'timestamp': ctime(time()),
        'data': {
            'humidity': {
                'value': 71.71,
                'unit': '%'
            },
            'temperature': {
                'value': 21.21,
                'unit': 'C'
            }
        }
    },
    {
        'id': 3,
        'timestamp': ctime(time()),
        'data': {
            'humidity': {
                'value': 72.72,
                'unit': '%'
            },
            'temperature': {
                'value': 22.22,
                'unit': 'C'
            }
        }
    }
]

dummy_sensor_read = {
    'id': 1,
    'data': [
        {
            'timestamp': ctime(time()),
            'data': {
                'humidity': {
                    'value': 72.72,
                    'unit': '%'
                },
                'temperature': {
                    'value': 22.22,
                    'unit': 'C'
                }
            }
        },
        {
            'timestamp': ctime(time()),
            'data': {
                'humidity': {
                    'value': 72.72,
                    'unit': '%'
                },
                'temperature': {
                    'value': 22.22,
                    'unit': 'C'
                }
            }
        },
        {
            'timestamp': ctime(time()),
            'data': {
                'humidity': {
                    'value': 72.72,
                    'unit': '%'
                },
                'temperature': {
                    'value': 22.22,
                    'unit': 'C'
                }
            }
        }
    ]
}

dummy_read_max = {
    'id': 1,
    'timestamp': ctime(time()),
    'data': {
        'humidity': {
            'value': 72.72,
            'unit': '%'
        },
        'temperature': {
            'value': 22.22,
            'unit': 'C'
        }
    }
}
