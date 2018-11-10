#!/usr/bin/env python3
"""
sockets.py - socketsio
"""


from flask_socketio import SocketIO, emit

socketio = SocketIO(app)


@sockets.route('/hello')
def hello():
    return 'Hello'


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 5000
    app.run(host=HOST, port=PORT)
