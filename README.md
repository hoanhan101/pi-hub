# pi-hub

**pi-hub** is a management system that stores temperature and humidity sensor readings from a 
collection of Raspberry Pi and uses a simple RESTful API to provide a simple monitoring solution.

## Project status

The project is complete. API is documented. Docker is available.

## Table of Contents

- [Getting Started](#getting-started)
- [Structure](#structure)
- [API](#api)
- [Sensor Workshop](#sensor-workshop)

## Getting Started

**Build and run Docker containers**
```sh
./compose.sh
```

**Verify with `curl`**
```sh
curl http://localhost:5000/test
```

See the [API documentation](#api) for more details.

### Structure

Filename | Description
--- | ---
[Dockerfile](Dockerfile) | Dockerfile for pi-hub server: install dependencies, setup MySQL and expose endpoints.
[compose.sh](compose.sh) | Script to orchestrate mysql-sever container and pi-hub server.
[config.py](config.py) | Global configurations hub.
[helper.py](helper.py) | Helper functions.
[hub.py](hub.py) | Main server logic using flask, contains a list of available endpoints.
[hub_test.py](hub_test.py) | Simple test for [hub.py](hub.py)
[install_requirements.sh](install_requirements.sh) | Install python dependencies.
[requirements.txt](requirements.txt) | Python dependencies.
[sample_client.py](sample_client.py) | Sample client who uses pi-hub.
[setup_mysql.py](setup_mysql.py) | Script to setup MySQL correctly: create database and setup tables.
[sql.py](sql.py) | List of available SQL functions using MySQL Connector.
[start.sh](start.sh) | Script for Docker container initialization, used by Dockerfile.

## API

**List of all available endpoints**

Method | Endpoint | Description
--- | --- | ---
GET/POST | `/test` | Test if the server is alive and reachable.
GET | `/config` | Get a list of configurations.
GET | `/scan` | Get a list of sensors with their locations.
GET | `/read/all` | Get a list of all sensor readings.
GET | `/read/max` | Get a maximum sensor readings.
GET | `/read/last_hour` | Get all reading from the last hour.
GET | `/read/last_hour/max` | Get a maximum reading from the last hour.
GET | `/read/yesterday` | Get all reading from yesterday.
GET | `/read/yesterday/max` | Get a maximum reading from yesterday.
GET | `/read/<int:id>` | Get all reading for a specific sensor.
GET | `/read/<int:id>/last_hour` | Get all reading for a specific sensor from the last hour.
GET | `/read/<int:id>/yesterday` | Get all reading for a specific sensor from yesterday.
POST | `/write` | Publish a sensor reading to the system.

**Sample responses**

```sh
/test
    {'status': 'ok', 'timestamp': 'Sat May 26 16:41:38 2018'}

/config
    {'debug': True,
     'mysql': {'database': 'sensor_workshop',
               'host': 'mysql1',
               'password': '',
               'port': 3306,
               'user': 'root'},
     'pretty_json': True,
     'url': 'http://54.172.51.227:5000'}

/scan
    {'sensors': [{'id': 5, 'location': 2}]}

/read/all
    [{'data': {'humidity': {'unit': '%', 'value': 60.1},
               'temperature': {'unit': 'C', 'value': 20.2}},
      'id': 5,
      'timestamp': '2018-05-26 16:41:28'}]

/read/max
    [{'data': {'humidity': {'unit': '%', 'value': 60.1},
               'temperature': {'unit': 'C', 'value': 20.2}},
      'id': 5,
      'timestamp': '2018-05-26 16:41:28'}]

/read/last_hour
    [{'data': {'humidity': {'unit': '%', 'value': 60.1},
               'temperature': {'unit': 'C', 'value': 20.2}},
      'id': 5,
      'timestamp': '2018-05-26 16:41:28'}]

/read/last_hour/max
    ditto

/read/yesterday
    ditto

/read/yesterday/max
    ditto

/read/1
    ditto

/read/1/last_hour
    ditto

/read/1/yesterday
    ditto

/write
    {'error': None, 'id': 1, 'timestamp': 'Sat May 26 16:41:39 2018'}
```

## Sensor Workshop

Install git if you have not:
```sh
sudo apt-get install git
```

Clone the project:
```sh
git clone https://github.com/hoanhan101/pi-hub.git
```

Copy your program file into pi-hub folder. For example, my program's name is `read_sensor.py`:
```sh
cp read_sensor.py pi-hub/read_sensor.py
```

Change directory to pi-hub and install dependencies:
```sh
cd pi-hub && ./install_requirements.sh
```

Adapt this code to your program:
```python

import time
import helper # This helper library will help us push the sensor reading to the collection server.

# Imagine your functions' definitions are here. Below is your main program.

# It will look similar to this.

# Define a variable name SENSOR_ID to save your sensor id. For example, my sensor id is 1. 
SENSOR_ID = 1

# Define your location, which is assigned by the visualization team. For example, my location is A10.
LOCATION = 'A10'

# Define how much time do you want to wait between each send to the server.
# Any value from 15 to 30 seconds is good enough. Below will be too much overhead for the server.
# You don't want to hurt the server, do you?
SLEEP_TIME = 15

# Loop forever.
while True:
    block = get_reading()
    temp = convert_temp_reading(block[0], block[1], mode='celsius')
    humidity = convert_humidity_reading(block[3], block[4])

    # Publish the sensor reading to the server, providing sensor id and its location.
    helper.post(SENSOR_ID, LOCATION, temp, humidity)

    # Sleep for some time then repeat.
    time.sleep(SLEEP_TIME)
```

After following these steps above, you should be able to send data to the server by executing:
```sh
./read_sensor.py
```

If you receive an output like this, it means that you have successfully pulish your reading to the
server:
```sh
{'error': None, 'id': 1, 'timestamp': 'Sat May 26 16:41:39 2018'}
```

Bravo!
