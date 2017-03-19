#coding:utf-8
import docx

class SimpRead(object):
	

	def __init__(self):
		pass

	def readdocx(self, filename):
		doc = docx.Document(filename)
		return doc.paragraphs
