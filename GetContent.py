#coding:utf-8
import docx

class SimpRead(object):
	

	def __init__(self):
		pass

	def read_docx(self, filename):
		doc = docx.Document(filename)
		return doc.paragraphs
