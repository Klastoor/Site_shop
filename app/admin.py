#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.models import Users, Products, Address
from app import app, db
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_login import current_user

from flask import redirect, url_for


class ModelViewSecured(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.email == app.config['ADMIN_EMAIL']
        return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('home'))


admin = Admin(app, name='Admin', template_mode='bootstrap3')
admin.add_view(ModelViewSecured(Users, db.session))
admin.add_view(ModelViewSecured(Products, db.session))
admin.add_view(ModelViewSecured(Address, db.session))