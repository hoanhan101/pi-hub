"""
"""

from sql_functions import *

insert_reading(1, 2, 20.0, 'C', 60.6)
print(get_all_readings())
print(get_readings_last_hour())
print(get_readings_yesterday())
print(get_readings_from_sensor(1))
print(get_readings_from_sensor(2))


clean_up_table()
print(get_all_readings())
