# project/server/models.py


import datetime

from flask import current_app

from project.server import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    confirmed = db.Column(db.Boolean, default=False, nullable=False)
    email_sent = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<User {0}>'.format(self.email)
