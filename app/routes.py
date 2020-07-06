#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import redirect, render_template, url_for, request, flash
from app import app, db
from app.forms import RegisterForm, LoginForm
from app.models import User
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.urls import url_parse

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(name=form.name.data, surname=form.surname.data, second_name=form.second_name.data, gender=form.gender.data, email=form.email.data)
        new_user.set_password(form.password_1.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Аккаунт успешно создан!" , category='info')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user_now =  User.query.filter_by(email = form.email.data).first()

        if user_now and user_now is not None:
            if user_now.check_password(form.password.data):
                login_user(user_now, remember=form.remember.data)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('home')
                return redirect(next_page)
            else:
                flash("Неверно  введен пароль!")       
        else:
            flash("Аккаунт с таким логином - нет!")
    return render_template("login.html", form=form)

@app.route('/user/<id>')
@login_required
def user(id):
    user = User.query.filter_by(id=int(id)).first_or_404()
    text = f"Покупатель {user.name} {user.surname} {user.second_name} числится под номером {user.id}"
    return render_template('user.html', posts=text)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("home")