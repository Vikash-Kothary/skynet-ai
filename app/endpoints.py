#!/usr/bin/env python3
"""
endpoints.py - API endpoints
"""

from flask import Blueprint, render_template, request
import json

api = Blueprint("endpoints", __name__)


users = {
    'trainstaff@example.com': {'email': 'trainstaff@example.com', 'password': 'trainstaff', 'type': 'trainstaff'},
    'trainstaff2@example.com': {'email': 'trainstaff2@example.com', 'password': 'trainstaff2', 'type': 'trainstaff'},
    'stationstaff@example.com': {'email': 'stationstaff@example.com', 'password': 'stationstaff', 'type': 'stationstaff'},
    'station2staff@example.com': {'email': 'station2staff@example.com', 'password': 'station2staff', 'type': 'stationstaff'}
}


@api.route('/login', methods=['GET', 'POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if email is not None and password is not None and users.get(email) is not None and users[email]['password'] == password:
        return json.dumps({'status': 'success', 'type': users[email]['password']})
    return json.dumps({'status': 'fail'})


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 5000
    app.run(host=HOST, port=PORT)
