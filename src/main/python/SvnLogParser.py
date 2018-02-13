#!/bin/python27
#
#
#	Parse an svn log in xml format 
#
#
#	Sample input: 
# 	svn log -v --xml https://github.com/concordion/idea-concordion-support > log1.xml
#	dee ${project_dir)/test/log1.xml
#
#
#	REFERENCE
#	https://docs.python.org/2/library/subprocess.html
#	http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.log.html
#	https://wiki.python.org/moin/Sax
#	https://docs.python.org/2/library/json.html
#
import xml.sax
import sys

from domain import ChangeList, Change


def extractIssueId(message):
	#TODO
	return "PRJ-1"

class SvnLogParser(xml.sax.ContentHandler):
	def __init__(self):
		self._model=[]
		self._tagStack=[]
	
	def getModel(self):
		return self._model

	def getCurrentEntry(self):
		return self._model.entries[-1] if self._model.entries else None

	def getCurrentTag(self):
		if self._tagStack: 
			return self._tagStack[-1]
		else: 
			return None
		
	def pushTag(self, tag):
		self._tagStack.append(tag)
	
	def popTag(self):
		return self._tagStack.pop()
		
	def parse(self, logfile):
		"""
		transform xml svn log to python object structure
		"""
		self.__init__()
		xml.sax.parse(logfile, self)
		
		return self.getModel()

	def startElement(self, name, attrs):
	
		self.pushTag(name)
	
		if name=="log":
			self.startLog()
		elif name=="logentry":
			self.startLogEntry(attrs)

	def endElement(self, name):
		if name=="log":
			self.endLog()
		elif name=="logentry":
			self.endLogEntry()
		
		self.popTag()
	
	
	def characters(self, content):
		if self.getCurrentTag()=="msg":
			self.processMsg(content)
		elif self.getCurrentTag()=="author":
			self.processAuthorContent(content)
		elif self.getCurrentTag()=="date":
			self.processDateContent(content)
		elif self.getCurrentTag()=="path":
			self.processPathContent(content)

	def startLog(self):
		self._model=ChangeList()

	def endLog(self):
		pass

	def startLogEntry(self, attrs):
		entry = Change(int(attrs["revision"]))
		self.getModel().entries.append(entry)

	def endLogEntry(self):
		pass

	def processMsg(self, content):
		self.getCurrentEntry().issue=extractIssueId(content)
		self.getCurrentEntry().comment=content
	
	def processAuthorContent(self, content):
		self.getCurrentEntry().author=content
	
	def processDateContent(self, content):
		self.getCurrentEntry().date=content
	
	def processPathContent(self,content):
		self.getCurrentEntry().paths.append(content)
	


if __name__ == "__main__":
	f = file.open(sys.argv[1])
	log = SvnLogParser().parse(f)
	print log
	
	

	
	
	