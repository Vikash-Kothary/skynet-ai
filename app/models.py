#!/usr/bin/env python3
"""
models.py - Defines models to represent data
"""

from app import db


class Queries(db.Model):
    __tablename__ = 'query_table'

    # Category
    QUESTION = 'question'
    LOST = 'lost'
    ASSISTANCE = 'assistance'

    query_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    created_by = db.Column(db.String)
    priority = db.Column(db.Integer)
    nearest_station = db.Column(db.String)
    nearest_staff_id = db.Column(db.String)
    category = db.Column(db.Enum(QUESTION, LOST, ASSISTANCE, name='category'))
    extra_data = db.Column(db.String)

    def __init__(self, title, created_by, priority=None, nearest_station=None, nearest_staff_id=None, category=None, extra_data=None):
        if priority == None:
            priority = 1
        if category == None:
            category == QUESTION
        self.title = title
        self.created_by = created_by
        self.priority = priority
        self.nearest_station = nearest_station
        self.nearest_staff_id = nearest_staff_id
        self.category = category
        self.extra_data = extra_data

    def __repr__(self):
        """Return an unambiguous representation of a product"""
        return '<Queries(query_id={}, title={}, created_by={}, priority={:.2f}, nearest_station={}, nearest_staff_id={}, category={}, extra_data={})>'.format(
            self.query_id, self.title, self.created_by, self.priority, self.nearest_station, self.nearest_staff_id, self.category, self.extra_data)


class User(db.Model):
    __tablename__ = 'user_table'

    # user_type
    PASSENGER = 'passenger'
    TRAIN_STAFF = 'train_staff'
    STATION_STAFF = 'station_staff'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_type = db.Column(db.Enum(PASSENGER, TRAIN_STAFF, STATION_STAFF, name='user_type'))

    def __init__(self, email, password, user_type=None):
        if user_type == None:
            user_type = User.PASSENGER
        self.email = email
        self.password = password
        self.user_type = user_type

    def __repr__(self):
        """Return an unambiguous representation of a product"""
        return '<User(email={}, password={}, user_type={})>'.format(
            self.email, self.password, self.user_type)
