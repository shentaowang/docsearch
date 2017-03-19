#coding:utf-8
import GetContent
import OperateEs
from datetime import datetime

filename = "testdoc/testdoc2.docx"
HOST = "127.0.0.1"
PORT = 9200
USERNAME = 'light'


read = GetContent.SimpRead()
es = OperateEs.Operate(HOST, PORT, USERNAME)


content  = read.read_docx(filename)
for line in content:
	print line.text


