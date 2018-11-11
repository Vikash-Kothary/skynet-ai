#!/usr/bin/env python3
"""
mock.py - Seperate mock util functions
"""


def generate_issue_id():
    return randint(10000, 999999)

users = {
    'trainstaff@example.com': {'email': 'trainstaff@example.com', 'password': 'trainstaff', 'type': 'trainstaff'},
    'trainstaff2@example.com': {'email': 'trainstaff2@example.com', 'password': 'trainstaff2', 'type': 'trainstaff'},
    'stationstaff@example.com': {'email': 'stationstaff@example.com', 'password': 'stationstaff', 'type': 'stationstaff'},
    'station2staff@example.com': {'email': 'station2staff@example.com', 'password': 'station2staff', 'type': 'stationstaff'}
}

dialogs = {
    "hi": "Hello!",
    "how are you?": "Fine and you",
    "fine": "Then have a good trip"
}

queries = {
    'node1': [
        {
            "issue_id": 12345,
            "resolved": 0,
            "title": "why so noisy?",
            "created_by": "user_socket_id1",
            "priority": 1,
            "nearest_station": "station1",
            "nearest_staff_id": "trainstaff@example.com",
            "category": "question",
            "extra_data": {}
        },
        {
            "issue_id": 12346,
            "resolved": 0,
            "title": "lost child",
            "created_by": "user_socket_id2",
            "priority": 5,
            "nearest_station": "station1",
            "nearest_staff_id": "trainstaff@example.com",
            "category": "lost",
            "extra_data": {}
        }
    ]
}
