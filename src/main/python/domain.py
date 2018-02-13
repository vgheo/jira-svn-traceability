'''
Created on Feb 10, 2018

@author: vlad

refs
https://stackoverflow.com/questions/9542738/python-find-in-list

'''


class IssuesSet:

    def __init__(self):
        self.issues = {}

    def add(self, issue):
        self.issues.update({issue.key:issue})

    def get(self, key):
        return self.issues.get(key, None)


class Issue:
    '''
    '''

    def __init__(self, key, url, issType, summary):
        self.key = key
        self.url = url
        self.type = issType
        self.summary = summary
        self.subtasks = []
        
# Issue structure


class Structure:

    def __init__(self):
        self.root = StructureNode(None)
    
    def find(self, key):
        return self.root.find(key)
             

class StructureNode:

    def __init__(self, key):
        self.key = key
        self.children = []

    def add(self, node):
        self.children.append(node)

    def allChildren(self):
        return self.children + [node for child in self.children for node in child.allChildren()]

    def find(self, key):
        return next((n for n in [self] + self.allChildren() if n.key == key), None)


class ChangeList:

    def __init__(self, basePath=""):
        '''
        @param basePath base path of the project. all paths in the set sre under this path
        '''
        self.entries = []
        self.basePath = basePath
        
    def add(self, entry):
        self.entries.append(entry)


class Change:

    def __init__(self, changeId, comment=None, paths=[], issue=None):
        self.id = changeId
        self.comment = comment
        self.paths = paths
        self.issue = issue

