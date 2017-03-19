#coding:utf-8

from elasticsearch import Elasticsearch

class Operate(object):
	def __init__(self,host,port):
		self.host = host
		self.port = port
		self.es = Elasticsearch([{'host':host,'port':port}])

	def 
