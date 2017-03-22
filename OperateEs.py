#coding:utf-8

from elasticsearch import Elasticsearch

class Operate(object):
	def __init__(self, host, port, username):
		self.host = host
		self.port = port
		self.username = username
		self.es = Elasticsearch([{'host':host,'port':port}])
 
	def create_index(self):
		self.es.indices.create(index = self.username)
	
	def mapping(self, doc_class):
		map_body = {
				"mappings":{
					"properties":{
						"content":{
							"type":"text",
							"analyzer":"ik_max_word",
							"include_in_all":"true",
							"bost":8
							}
						}
					}
				
				}
		self.es.index(index = self.username,doc_type = doc_class,body = map_body)
	
	def insert_doc(self, content):
		insert_body = {
				
				}
	
	def query_settings(self, index_name):
		print self.es.indices.get_settings(index = index_name)


	def simple_search(self, username):
		#return self.es.get("index" = self.username)['_source']
		pass
