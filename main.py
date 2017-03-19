#coding:utf-8
import GetContent
from elasticsearch import Elasticsearch
from datetime import datetime

filename = "testdoc/testdoc2.docx"
host = "127.0.0.1"
port = 9200

es = Elasticsearch([{'host':host, 'port':port}])
es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
print es.get(index="my-index", doc_type="test-type", id=42)['_source']

read = GetContent.SimpRead()
content  = read.readdocx(filename)
for line in content:
	print line.text

