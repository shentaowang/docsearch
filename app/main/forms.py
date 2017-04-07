#-*- coding:utf-8 -*-
# Author:lightwang.96@gmail.com
# github:https://github.com/GeniusLight/docsearch

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email

class NameForm(Form):
    name = StringField('what is you name?', validators=[Required()])
    submit = SubmitField('submit')

class LoginForm(Form):
    email = StringField('Email', validators=[Required(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[Required()])
    submit = SubmitField('Log IN')
