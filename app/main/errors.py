#-*- coding:utf-8 -*-
# Author:lightwang.96@gmail.com
# github:https://github.com/GeniusLight/docsearch

from flask import render_template
from . import main

@main.app_errorhandle(404)
def page_not_found(e):
    return render_template("404.html"), 404

@main.app_errorhandle(500)
def internal_server_error(e):
    return render_template("500.html"), 500

