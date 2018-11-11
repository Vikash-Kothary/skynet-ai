#!/usr/bin/env python3
"""
sockets.py - socketsio
"""


from flask_socketio import SocketIO, emit
from flask import request
from app import app, db
import chatbot
from random import randint
import mock
from models import Query
import requests as r

socketio = SocketIO(app)


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('query')
def handle_query_event(json, methods=['GET', 'POST']):
    current_socket_id = request.sid
    room_id = 'node1'
    if not any([i.get('created_by') == current_socket_id for i in mock.queries.get(room_id, [])]):
        pass
        # create a new query
        new_query = Query()
        new_query.title = json.get('message', 'no title')
        new_query.created_by = current_socket_id
        new_query.nearest_station = 'station1'
        new_query.nearest_staff_id = 'trainstaff@example.com'
        new_query.category = Query.QUESTION
        new_query.room_id = 'node1'
        db.save(new_query)
        # mock.queries[room_id].append(new_query.to_json())
        # Confirm received query
    print(json)
    message = r.get('http://78e50db0.ngrok.io/?q=' + json.get('message')).text
    chatbot.confirm_received_query(message)
    socketio.emit('query_response', new_query.to_json(), callback=messageReceived)


@socketio.on('get_queries')
def handle_query_event(json, methods=['GET', 'POST']):
    current_socket_id = request.sid
    room_id = json.get('room_id')
    # room_queries = [q for q in mock.queries.get(room_id, []) if q.get('resolved') == 0]
    query_result = Query.query.filter_by(
        room_id='node1', resolved=False).filter(category != Query.QUESTION)
    room_queries = [query_result[i].to_json() for i in range(query_result.count())]
    socketio.emit('get_queries_response', {'current_socket_id': current_socket_id,
                                           'queries': room_queries, 'room_id': room_id}, callback=messageReceived)


@socketio.on('resolve')
def handle_resolve_event(json, methods=['GET', 'POST']):
    current_socket_id = request.sid
    issue_id = json.get('issue_id')
    current_queries = [q for qs in queries.values() for q in qs if q.get('issue_id') == issue_id]
    if current_queries:
        current_query = current_queries[0]
        current_query['resolved'] = 1
        message = 'We resolved the issue. Thanks for using the service!'
        socketio.emit('query_response', {'current_socket_id': current_socket_id,
                                         'message': message, 'room_id': room_id}, callback=messageReceived)


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 5000
    app.run(host=HOST, port=PORT)
