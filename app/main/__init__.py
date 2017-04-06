#-*- coding:utf-8 -*-
# Author:lightwang.96@gmail.com
# github:https://github.com/GeniusLight/docsearch

from flask import Blueprint

main = Blueprint("main",__name__)

from .import views, errors
