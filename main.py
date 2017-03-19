#coding:utf-8
import getcontent

filename = "testdoc/testdoc2.docx"

read = getcontent.SimpRead()
content  = read.readdocx(filename)
for line in content:
	print line.text

