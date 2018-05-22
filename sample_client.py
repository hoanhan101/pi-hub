"""
    sample_client.py - Sample client code to send sensor readings to the collection server.
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/10/2018
"""

import time

from config import SENSOR_ID, FREQUENCY
from publisher import Publisher

def get_sample_reading():
    """
    Return sample temperature and humidity reading data.
    This models after get_reading() function we have already written. Use the get_reading function
    you've written instead of this in the main program below.
    
    Params:
        None

    Return:
        A tuple of temperature and humidity value in float.
    """
    sample_temperature = 20.2
    sample_humidity    = 60.6
    return sample_temperature, sample_humidity

if __name__ == '__main__':
    # Initialize our Publisher object to publish data to the hub.
    worker = Publisher()

    # Loop forever.
    while True:
        # Get sensor reading <Use your get_reading function here>
        sample_temperature, sample_humidity = get_sample_reading()

        # Sample POST data.
        sample_data = {
            'id': SENSOR_ID,
            'data': {
                'temperature': {
                    'value': sample_temperature,
                    'unit': 'C'
                },
                'humidity': {
                    'value': sample_humidity,
                    'unit': '%'
                }
            }
        }

        # Publish reading data to the hub using publish method.
        worker.publish(sample_data)

        # Sleep for a while before executing the next send.
        time.sleep(FREQUENCY)
