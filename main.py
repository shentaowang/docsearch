#coding:utf-8
import GetContent
import OperateEs
from datetime import date
from elasticsearch import Elasticsearch
import uuid


filename = "testdoc/testdoc2.docx"
HOST = "127.0.0.1"
PORT = 9200
USERNAME = 'light'
DOCTYPE = "word"

main_es = Elasticsearch(hosts=[{"host":HOST, "port":PORT}])
class_es = OperateEs.Operate(HOST, PORT, USERNAME)
read_content = GetContent.SimpRead()
#class_es.initial()

#print main_es.indices.get_mapping(index=USERNAME)
doc_name = "test"
path = None
content = read_content.read_docx(filename)
weight = 1
insert_time = date.today()
remark = None
query = ""


insert_body = {
		"doc_name" : doc_name,	
		"path" : path,
		"content" : content,
		"weight" : weight,
		"insert_time" : insert_time,
		"remark" : remark		
		}

#main_es.create(index=USERNAME, doc_type=DOCTYPE, id=uuid.uuid1(), body=insert_body)


search_body = {
		"query":{
			"match":{
				"content":"在时间的无涯"
				}
			},
			"highlight":{
				"pre_tags":["<tag1>", "<tag2>"],
				"post_tags":["</tag1>", "</tag2>"],
				"fields":{
					"content":{}
					}
			}
		}
result = main_es.search(index=USERNAME, body=search_body)
for hit in result["hits"]["hits"]:
	print hit["_source"]["path"]
	print hit["_source"]["insert_time"]
	print hit["highlight"]["content"][0]




