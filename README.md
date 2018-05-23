# pi-hub

PiHub is a central management system that stores temperature and humidity sensors reading.

## Project status

It is an on-going project. Here is the link to our [design 
document](https://docs.google.com/document/d/1w93jYpGjRjTiokhEnTv7tspONa8558e2vc17fk6wqV0/edit?usp=sharing).

## Table of Contents

- [Server](#server)
- [Client](#client)

## Server

### Docker

**Quick way**

```
docker run -p 5000:5000 -dit --restart unless-stopped hoanhan/pi-hub
```

**Build and run**

```
docker build -t pi-hub . && docker run -p 5000:5000 -ti pi-hub
```

Can run `python3 sample_client.py` to test in both ways.

### Local

Clone the project and install dependencies:
```
git clone https://github.com/hoanhan101/pi-hub.git && cd pi-hub && ./install_requirements.sh
```

- Configure in [config.py](config.py). 
- Run the server by `python3 hub.py`
- Run the sample client program by `python3 sample_client.py`

## Client

Install git if you have not:
```
sudo apt-get install git
```

Clone the project and install dependencies:
```
git clone https://github.com/hoanhan101/pi-hub.git && cd pi-hub && ./install_requirements.sh
```

Configure the URL in [config.py](config.py) to `TBA`

Adapt the template and code in [sample_client.py](sample_client.py) to your main program.

After following these steps above successfully, you should be able to send data to the server.
