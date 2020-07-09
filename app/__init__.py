#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from logging.handlers import RotatingFileHandler
import os, logging
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
app.config.from_pyfile('../config.py')
run_with_ngrok(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
lm = LoginManager(app)
ckeditor = CKEditor(app)
lm.login_view = 'login'

# setings logs
if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/service.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Flask started...')

from app import routes, admin