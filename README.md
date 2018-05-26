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
```
./compose.sh
```

**Verify with `curl`**
```
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
GET/POST | /test | Test if the server is alive and reachable.
GET | /config | Get a list of configurations.
GET | /scan | Get a list of sensors with their locations.
GET | /read/all | Get a list of all sensor readings.
GET | /read/max | Get a maximum sensor readings.
GET | /read/last_hour | Get all reading from the last hour.
GET | /read/last_hour/max | Get a maximum reading from the last hour.
GET | /read/yesterday | Get all reading from yesterday.
GET | /read/yesterday/max | Get a maximum reading from yesterday.
GET | /read/<id:int> | Get all reading for a specific sensor.
GET | /read/<id:int>/last_hour | Get all reading for a specific sensor from the last hour.
GET | /read/<id:int>/yesterday | Get all reading for a specific sensor from yesterday.
POST | /write | Publish a sensor reading to the system.

**Sample responses**

```
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
    [{'data': {'humidity': {'unit': '%', 'value': 60.1},
               'temperature': {'unit': 'C', 'value': 20.2}},
      'id': 5,
      'timestamp': '2018-05-26 16:41:28'}]

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
```
sudo apt-get install git
```

Clone the project and install dependencies:
```
git clone https://github.com/hoanhan101/pi-hub.git && cd pi-hub && ./install_requirements.sh
```

Copy your program file into this folder:
```
cp <your_file_name>.py pi-hub/<your_file_name>.py
``

Adapt the template and code in [sample_client.py](sample_client.py) to your main program.

After following these steps above successfully, you should be able to send data to the server.
