#!/usr/bin/env python3
"""
endpoints.py - API endpoints
"""

from flask import Blueprint, render_template

api = Blueprint("endpoints", __name__)


@api.route('/hello')
def hello():
    return 'Hello'


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 5000
    app.run(host=HOST, port=PORT)
