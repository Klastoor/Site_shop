#!usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, IntegerField, StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, InputRequired, Email, Length, ValidationError, EqualTo, NumberRange
from app.models import Users
from flask_ckeditor import CKEditorField


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
        user = Users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Указанный почт.адрес неподходит, тк уже зарегистрирован!')

######################### Login
class LoginForm(FlaskForm):
    email = StringField('Почта: ', validators=[InputRequired(), Length(min=4, max=50)])
    password = PasswordField('Пароль: ', validators=[InputRequired()])
    remember = BooleanField('Запомнить меня: ', default='checked')
    btn = SubmitField('Войти')

class ProductForm(FlaskForm):
    name = StringField('Название товара', validators=[DataRequired(message="Наименование обязатльно!"), Length(min=3, message="Название должно состоять минимум из трех символов!")])
    descript = CKEditorField('Описание товара', validators=[DataRequired(message="Необходимо предоставить хотя бы короткое описание товара!"), Length(min=12, message="Еще чутка больше слов и сойдет!")])
    price = IntegerField("Цену необходимо указать в рублях!", validators=[DataRequired('Необходимо указать цену за один товар!'), NumberRange(min=999, message="Цена за единицу товара, не может быть меньше 999 руб!")])
    amount = IntegerField('Количество товара на складе', validators=[InputRequired(), NumberRange(min=0, max=500, message="Количество товаров должно варьироваться от 0 до 500 штук!")])