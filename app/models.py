#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from app import db, lm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    second_name = db.Column(db.String(64))
    gender = db.Column(db.String(20))
    password_hash = db.Column(db.String(120))
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    address = db.relationship('Address', backref='user', lazy='dynamic', primaryjoin="Users.id == Address.user_id")
   
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
	    return "<Пользователь № {}: {} {}>".format(self.id, self.name, self.surname)

    @lm.user_loader
    def load_user(user_id):
        return db.session.query(Users).get(user_id)

class Address(db.Model):
    __tablename__ = "Address_users"
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String())
    city = db.Column(db.String())
    street = db.Column(db.String())
    house_number = db.Column(db.Integer())
    address_index = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

class Products(db.Model):
    __tablename__ = "Products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    descript = db.Column(db.String)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)

