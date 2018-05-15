"""
    hub.py - PiHub server
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/10/18
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from time import time, ctime

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET', 'POST'])
def test():
    """
    Test endpoint.
    """
    if request.method == 'GET':
        response = {
            'timestamp': ctime(time()),
            'status': 'ok'
        }
    elif request.method == 'POST':
        response = {
            'timestamp': ctime(time()),
            'status': 'ok',
            'data': request.get_json()
        }

    return jsonify(response)


if __name__ == '__main__':
    app.run()
