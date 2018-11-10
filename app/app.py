#!/usr/bin/env python3
"""
app.py - Flask application
"""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)
app.config['SECRET_KEY'] = 'secret!'


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@app.route('/send_message/<text>', methods=['GET', 'POST'])
@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    pass
