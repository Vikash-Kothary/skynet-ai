#!/usr/bin/env python3
"""
endpoints.py - API endpoints
"""

from flask import Blueprint, render_template, request
import json
from data import users

api = Blueprint("endpoints", __name__)


@api.route('/login', methods=['GET', 'POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if email is not None and password is not None and users.get(email) is not None and users[email]['password'] == password:
        room_id = 'node1'
        return json.dumps({'status': 'success', 'type': users[email]['type'], 'room_id': room_id})
    return json.dumps({'status': 'fail'})


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 5000
    app.run(host=HOST, port=PORT)
