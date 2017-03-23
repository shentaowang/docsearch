#coding:utf-8
import GetContent
import OperateEs
from datetime import datetime
from elasticsearch import Elasticsearch

filename = "testdoc/testdoc2.docx"
HOST = "127.0.0.1"
PORT = 9200
USERNAME = 'light'

es = Elasticsearch([{"host":HOST, "port":PORT}])

#create the index 
#doc_index = es.indices.create(index=USERNAME)
#print doc_index


#get the mapping
#doc_mapping = es.indices.get_mapping(index=USERNAME)
#print doc_mapping


read = GetContent.SimpRead()

content  = read.read_docx(filename)
for line in content:
	print line.text


