#!/usr/bin/env python3
"""
chatbot.py - Natural language interface
"""

from models import Query


def confirm_received_query():
    return "We've received your request."


def check_assistance(new_query):
    if new_query.category == Query.ASSISTANCE:
        if new_query.nearest_station == None:
            return 'Where would you like assistance?'
        if new_query.nearest_staff_id != None:
            return 'Assistance will be provided at {}'.format(new_query.nearest_station)

def get_nlu_response():
	pass
