"""
    sample.py - Sample code using Publisher to push sensor readings to the hub.
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/10/2018
"""

from time import time, ctime
from publisher import Publisher

if __name__ == '__main__':
    # Sample sensor reading
    sample_data = {
        'id': 101,
        'data': {
            'temperature': {
                'value': 25.0,
                'unit': 'C'
            },
            'humidity': {
                'value': 60.0,
                'unit': '%'
            }
        }
    }

    worker = Publisher()

    print(worker.get('test'))
    print(worker.publish('write', sample_data))
