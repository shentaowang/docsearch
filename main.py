#coding:utf-8
import GetContent
import OperateEs
from datetime import datetime
from elasticsearch import Elasticsearch

filename = "testdoc/testdoc2.docx"
HOST = "127.0.0.1"
PORT = 9200
USERNAME = 'light'

main_es = Elasticsearch([{"host":HOST, "port":PORT}])
class_es = OperateEs.Operate(HOST, PORT, USERNAME)
read_content = GetContent.SimpRead()
#class_es.initial()

#print main_es.indices.get_mapping(index=USERNAME)
doc_name = "test"
path = None
content = read_content.read_docx(filename)
weight = 1
insert_time = datetime.now()
remark = None
print content




insert_body = {
		"doc_name" : doc_name,	
		"path" : path,
		"content" : content
		}
