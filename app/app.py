#!/usr/bin/env python3
"""
app.py - Flask application
"""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)
app.config['SECRET_KEY'] = 'secret!'

if __name__ == '__main__':
    pass
