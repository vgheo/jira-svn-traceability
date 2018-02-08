#!/bin/python27
#
#
#	Produces a report of the svn log for the given URL
# 	Output format : JSON
#
#	{ "revisions" : [
#		{ "id":"3", "issues" : [ "ID-9"] , "headline" : "ID-9 some comment", "branch" : "trunk"},
#		<...>
#	]}
#		
#		
#
#	
#	ENVIRONMENT
#	- svn available on PATH
#
#	REFERENCE
#	https://docs.python.org/2/library/subprocess.html
#	http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.log.html
#	https://wiki.python.org/moin/Sax
#	https://docs.python.org/2/library/json.html
#
import subprocess, shlex
import xml.sax
import sys
import json

def svn_log(url):
	svn_command = "svn log {0} ".format(url)
	p=subprocess.Popen(shlex.split(svn_command, stdout=subprocess.PIPE))
	return p.communicate()

def extractIssueId(message):
	#TODO
	return "ID-1"

class LogTransformer(xml.sax.ContentHandler):

	def __init__(self, out):
		self._out=out
		self._tagStack=[]

	def getCurrentTag(self):
		if len(self._tagStack)==0:
			return None
		else:
			return self._tagStack[-1]

	def startElement(self, name, attrs):
	
		self._tagStack.append(name)
	
		if name=="log":
			self.startLog()
		elif name=="logentry":
			self.startLogEntry(attrs)

	def endElement(self, name):
		if name=="log":
			self.endLog()
		elif name=="logentry":
			self.endLogEntry()
		self._tagStack.pop()
	
	def characters(self, content):
		if self.getCurrentTag() in ["msg"]:
			self.processMsg(content)
			
	def startLog(self):
		self._out.write('{ "revisions" : [\n')

	def endLog(self):
		self._out.write(']}') 

	def startLogEntry(self, attrs):
		self._entry = { "id" : attrs["revision"] }
	
	def endLogEntry(self):
		self._out.write(json.dumps(self._entry) )
		self._entry=None

	def processMsg(self, content):
		issueId = extractIssueId(content);
		
		self._entry.update( issues=[issueId] )
		self._entry.update( headline = content)	


def transform_log(log_xml):
	"""
	transform xml svn log to JSON log
	"""
	xml.sax.parseString(log_xml, LogTransformer(sys.stdout))

TEST_LOG="""
<log>
<logentry
   revision="1">
<author>harry</author>
<date>2008-06-03T06:35:53.048870Z</date>
<msg>Initial Import.</msg>
</logentry>
</log>
"""

def extract(url):
	#log_xml=svn_log(url)
	log_xml=TEST_LOG
	transform_log(log_xml)


if __name__ == "__main__":
	extract(sys.argv[1])
	
	
	