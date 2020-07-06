#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from app import db, lm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True, nullable=False)
    surname = db.Column(db.String(40), index=True, nullable=False)
    second_name = db.Column(db.String(40), index=True)
    email = db.Column(db.String(40), index=True, nullable=False, unique=True)
    gender = db.Column(db.String(20))
    password_hash = db.Column(db.String(120))
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
      

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
	    return "<Пользователь № {}: {} {}>".format(self.id, self.name, self.surname)

    @lm.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)
