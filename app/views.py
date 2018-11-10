#!/usr/bin/env python3
"""
views.py - Serve webpages
"""

from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route('/')
def dev():
    return render_template('dev.html')

if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 5000
    app.run(host=HOST, port=PORT)
