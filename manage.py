#-*- coding:utf-8 -*-
# Author:lightwang.96@gmail.com
# github:https://github.com/GeniusLight/docsearch

#!usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from elasticsearch import Elasticsearch, Transport
from config import ES_HOST, ES_PORT, map_body, ALLOWED_EXTENSIONS

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

es = Elasticsearch([{'host':ES_HOST, 'port':ES_PORT}])
for index_type in ALLOWED_EXTENSIONS:
    try:
        es.indices.get_mapping(index=index_type)
    except Exception as e:
        es.indices.create(index=index_type, body=map_body)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    manager.run()
