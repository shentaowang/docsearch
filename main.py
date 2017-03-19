#coding:utf-8
import getcontent

filename = "testdoc/testdoc1.doc"

read = getcontent.SimpRead()
content  = read.readdocx(filename)
for line in content:
	print line.text

