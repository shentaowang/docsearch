#-*- coding:utf-8 -*-
# Author:lightwang.96@gmail.com
# github:https://github.com/GeniusLight/docsearch

import os
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = '/path/to/the/upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'docx'])
ES_HOST = "127.0.0.1"
ES_PORT = 9200

map_body = {
	"mappings":{
		"word":{
			"_all":{
				"analyzer":"ik_max_word",
        		"search_analyzer":"ik_max_word",
				"term_vector":"no",
				"store":"false"
			},
			"properties":{
				"doc_name":{
			        "type":"text",
					"analyzer":"ik_max_word",
					"include_in_all":"true",
					"boost":8
			},
			    "path":{
				    "type":"text",
				    "analyzer":"ik_max_word",
				    "include_in_all":"true",
				    "boost":8
			    },
			    "content":{
				    "type":"text",
				    "analyzer":"ik_max_word",
			    	"include_in_all":"true",
			    	"boost":8
		    	},
		    	"importance":{
			    	"type":"integer"
		    	},
		    	"insert_time":{
			    	"type":"date",
			    	"format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
		    	},
		    	"remark":{
			    	"type":"text"
			    }
		    }
	    }
    }
}


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_SLOW_DB_QUERY_TIME=0.5
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
            'sqlite:///'+os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
            'sqlite:///'+os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///'+os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
