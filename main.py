#coding:utf-8
import GetContent
import OperateEs
from datetime import date
from elasticsearch import Elasticsearch

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

#main_es.create(index=USERNAME, doc_type=DOCTYPE, id=1, body=insert_body)


search_body = {
		"query":{
			"match":{
				"content":"搜索"
				}
			},
			"highlight":{
				"pre_tags":["<tag1>", "<tag2>"],
				"post_tags":["</tag1>", "/tag2"],
				"fields":{
					"content":{}
					}
			}
		}
print main_es.search(index=USERNAME, body=search_body)



