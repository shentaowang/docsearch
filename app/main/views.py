#-*- coding:utf-8 -*-
# Author:lightwang.96@gmail.com
# github:https://github.com/GeniusLight/docsearch

from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/',methods=['GET','POST']))
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        #好像还有很多要写
        return url_for(".index")
    return render_template('index.html',
                          form=form, name=session.get('name'),
                          known=session.get('known', false),
                          current_time=datetime.utcnow())

