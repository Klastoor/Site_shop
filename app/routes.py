from flask import redirect, render_template, url_for, request, flash
from app import app, db
#from app.forms import RegisterForm, LoginForm
from app.models import User
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.urls import url_parse

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")