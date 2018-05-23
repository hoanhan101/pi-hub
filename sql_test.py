"""
    sql_test.py - Test sql functions.
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/23/18
"""

import random
from pprint import pprint

from sql_functions import *

# Create a bunch of dummy data
# for i in range(0, 30):
#     insert_reading(random.randint(0, 20),
#                    random.randint(0, 20),
#                    random.uniform(10, 30),
#                    'C',
#                    random.uniform(50, 70))
# pprint(get_all_readings())

# print('Clean up the table')
# clear_table()
# pprint(get_all_readings())


# Avaiable functions
print(get_readings_last_hour())
# print(get_readings_yesterday())
# print(get_readings_from_sensor(1))
# print(get_readings_from_sensor(2))
# print(get_readings_yesterday_by_id(1))
# print(get_readings_last_hour_by_id(1))
# print(get_max_reading_yesterday())
# print(get_max_reading_last_hour())
# print(get_sensor_and_location())
