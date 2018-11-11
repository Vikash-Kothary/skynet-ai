#!/usr/bin/env python3
"""
app.py - Flask application
"""

import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='')
    CORS(app)
    app.config['SECRET_KEY'] = 'secret!'
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(basedir, 'default.sqlite'))
    return app


def create_db(app):

    def _init_db():
        with app.app_context():
            db.drop_all()
            db.create_all()

    def _save_util(user=None):
        if user:
            db.session.add(user)
        db.session.commit()

    def _clear_data():
        session = db.session
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            session.execute(table.delete())
        session.commit()

    db = SQLAlchemy()
    db.init_app(app)
    db.create_tables = _init_db
    db.save = _save_util
    db.clear_all = _clear_data
    return db

app = create_app()
db = create_db(app)

if __name__ == '__main__':
    pass
