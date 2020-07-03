#!/usr/bin/env python3
from random import choice, sample

def check(checklist:list)->list:
    """ Removes variants where is not number and/or all letters in one case"""
    new_checklist=[]
    for item in checklist:
        new_checklist.append(None) if not any(map(str.isdigit, list(item))) else new_checklist.append(item)
        new_checklist.append(None) if not any(map(str.title, list(item))) or all(map(str.title, list(item))) else new_checklist.append(item)
    new_checklist = [x for x in new_checklist if x is not None]
    return new_checklist

def computation(loop:str, round:str, string:str) -> list:
    """ generate password from response parametrs """
    words = []
    for i in range(int(loop)*10):
        letters = []
        for j in range(128):
            j = choice(string)
            letters.append(j)
        word = "".join(sample(letters,int(round)))
        words.append(word)
    words = list(set(check(words)))
    result = sample(words, int(loop))
    return list(map(lambda x: {'id': 'item_'+str(x[0]), 'password': str(x[1])} , enumerate(result)))

password = computation("20", "20", "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!#(=%)")
password = password[0]['password']

info = f"""from os import path

URI = path.abspath(path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(URI, 'app/app.db')
LOGIN_MESSAGE = 'Сперва необходимо войти в систему!'
REFRESH_MESSAGE = 'Пожалуйста перезайдите в систему!'
SECRET_KEY = '{password}'
TESTING = True
DEBUG = True
FLASK_ENV = 'development'
"""

with open("config.py", "w", encoding='UTF-8') as f:
    f.write(f"{info}")