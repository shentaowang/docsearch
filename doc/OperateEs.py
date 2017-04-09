#coding:utf-8

from elasticsearch import Elasticsearch

class Operate(object):
	def __init__(self, host, port, username):
		self.host = host
		self.port = port
		self.username = username
		self.es = Elasticsearch([{'host':host,'port':port}])
	
	def initial(self):
		if self.es.indices.exists(index=self.username):
			self.es.indices.delete(index=self.username)
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
			self.es.indices.create(index=self.username,body=map_body)

