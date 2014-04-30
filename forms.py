# -*- coding: utf-8 -*-
__author__ = 'bglebov'

from flask_wtf import Form, RecaptchaField
from wtforms import StringField
from wtforms.validators import required, email


class SignUpForm(Form):
    lastname = StringField(u'Фамилия', [required()])
    firstname = StringField(u'Имя', [required()])
    company = StringField(u'Компания', [required()])
    position = StringField(u'Должность', [required()])

    phone = StringField(u'Контактный телефон', [required()])
    email = StringField(u'Адрес электронной почты', [required(),
                                                     email()])

    #recaptcha = RecaptchaField()