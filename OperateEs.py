#coding:utf-8

from elasticsearch import Elasticsearch

class Operate(object):
	def __init__(self, host, port, username):
		self.host = host
		self.port = port
		self.username = username
		self.es = Elasticsearch([{'host':host,'port':port}])
 
	def create_index():
		self.es.indices(index = self.username)

	def simple_search(self, username):
		#return self.es.get("index" = self.username)['_source']
		pass
