#encoding:utf-8
import docx
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class SimpRead(object):
	

	def __init__(self):
		pass

	def read_docx(self, filename):
		doc = docx.Document(filename)
		paragraphs = []
		for i in doc.paragraphs:
			paragraphs.append(i.text.encode("utf-8"))
		content = "\n".join(paragraphs)
		return content
