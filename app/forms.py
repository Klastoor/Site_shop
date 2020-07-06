#!usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField, TextAreaField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, InputRequired, Email, Length, ValidationError, EqualTo
from app.models import User


################# Registr
class RegisterForm(FlaskForm):
    name = StringField('Имя: ', validators=[DataRequired()])
    surname = StringField('Фамилия: ', validators=[DataRequired()])
    second_name = StringField('Отчество (не обязательно): ')
    gender = SelectField('Вы: ',validators=[DataRequired()] , choices=[('men', 'мужчина'), ('women', 'женщина')])
    email = EmailField('Ваша почта: ', validators=[DataRequired(), Email(message='Указанная почта уже была использована!'), Length(max=50)])
    password_1 = PasswordField('Новый пароль: ',  validators=[DataRequired(), Length(min=6, max=20, message='Пароль должен состоять от 6 до 20 символов!')])
    password_2 = PasswordField('Повтор пароля: ', validators=[DataRequired(), EqualTo('password_1', message='Пароли не совпадают!')]) 
    btn = SubmitField('Подтвердить')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Указанный почт.адрес неподходит, тк уже зарегистрирован!')

######################### Login
class LoginForm(FlaskForm):
    email = StringField('Почта: ', validators=[InputRequired(), Length(min=4, max=50)])
    password = PasswordField('Пароль: ', validators=[InputRequired()])
    remember = BooleanField('Запомнить меня: ', default='checked')
    btn = SubmitField('Войти')
