"""
    sample_client.py - Sample client code to send sensor readings to the collection server.
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/10/2018
"""

import time

from helper import post

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
    # Configurations
    SENSOR_ID = 1
    LOCATION = 2
    SLEEP_TIME = 5

    # Loop forever.
    while True:
        # Get sensor reading <Use your get_reading function here>
        sample_temperature, sample_humidity = get_sample_reading()

        post(SENSOR_ID, LOCATION, sample_temperature, sample_humidity)

        time.sleep(SLEEP_TIME)
