'''
Created on Feb 10, 2018

@author: vlad
'''
from samba.dcerpc.epmapper import EPMAPPER_STATUS_NO_MORE_ENTRIES

class Issue:
    '''
    '''

    def __init__(self, key, summary):
        self._key=key
        self._summary=summary
        
        
# Issue structure


class StructureNode:
    
    def __init__(self, key, children):
        self.key=key
        self.children=children
    


class SvnLog:
    def __init__(self):
        self._entries=[]

    def entries(self):
        self._entries
        
    def add(self, entry):
        self._entries.append(entry)


class SvnLogEntry:
    def __init__(self, revision, comment, paths, jiraId ):
        self._revision=revision
        self._comment=comment
        self._paths=paths
        self._jiraId=jiraId
        
    def revision(self): self._revision
    def comment(self): self._comment
    def paths(self): self._paths
    def jiraId(self): self._jiraId

