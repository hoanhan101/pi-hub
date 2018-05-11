# pi-hub

PiHub is a central management system that stores temperature and humidity sensors reading 
and displays visualization.

## Project status

It is an on-going project. Here is the link to our design document: [Design
Doc](https://docs.google.com/document/d/1w93jYpGjRjTiokhEnTv7tspONa8558e2vc17fk6wqV0/edit?usp=sharing)

## Usage

- Clone the project: `git clone https://github.com/hoanhan101/pi-hub.git`
- Install dependencies: `./install_requirements.sh`
- Configure in [config.py](config.py). At the moment, only URL is configurable. Default is
  localhost at port 5000.
- Run the server by `python3 hub.py`
- Run the sample client program by `python3 sample.py`
