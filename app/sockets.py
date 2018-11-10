#!/usr/bin/env python3
"""
sockets.py - socketsio
"""


from flask_socketio import SocketIO, emit
from flask import request
from app import app

socketio = SocketIO(app)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('query')
def handle_query_event(json, methods=['GET', 'POST']):
    current_socket_id = request.sid
    print('received query: ' + str(json))
    json.update()
    socketio.emit('query_response', {'current_socket_id': current_socket_id, 'message': 'Your query received. Thanks!'}, callback=messageReceived)


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 5000
    app.run(host=HOST, port=PORT)
