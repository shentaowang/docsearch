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

#create the mapping
map_body = {
		"settings":{
			"number_of_shards":1
			},
		"mappings":{
			"pdf":{
				"_all":{
					"analyzer":"ik_max_word",
					"search analyzer":"ik_max_word",
					"term_vector":"no",
					"store":"false"
					},
				"properties":{
					"content":{
						"type":"text",
						"store":"no",
						"term_vector":"with_positions_offsets",
						"analyzer":"ik_max_word",
						"include_in_all":"true",
						"boost":8
						}
					}
				}
			}
		}
doc_map = es.create(index=USERNAME, body=map_body)
print doc_map


#insert the data
insert_body = {
		"content":"美国留给中国是个烂摊子吗？,美国"
		}
#doc_insert = es.create(index=USERNAME, doc_type="pdf", id=1, body=insert_body)
#print doc_insert


#query the data
search_body = {
		"query":{
			"term":{
				"content":"中"
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
#doc_search = es.search(index=USERNAME, body=search_body)
#print doc_search


#get the mapping
#doc_mapping = es.indices.get_mapping(index=USERNAME)
#print doc_mapping


#delete the index
#print es.indices.delete(index=USERNAME)


read = GetContent.SimpRead()

content  = read.read_docx(filename)
for line in content:
	print line.text


