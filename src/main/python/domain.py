'''
Created on Feb 10, 2018

@author: vlad
'''

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
        self.entries=[]
        
    def add(self, entry):
        self.entries.append(entry)


class SvnLogEntry:
    def __init__(self, revision, comment, paths, jiraId ):
        self.revision=revision
        self.comment=comment
        self.paths=paths
        self.jiraId=jiraId
        
