'''
Created on Feb 10, 2018

@author: vlad
'''

import csv
import xml.dom.minidom


from domain import Structure, StructureNode, IssuesSet, Issue
from xml.dom.minidom import Node

class StructureBuilder:
    def __init__(self):
        self._nodeStack=[]
        self._structure = Structure()

    def getResult(self):
        return self._structure

    def top(self):
        return self._nodeStack[-1] if self._nodeStack else None
    
    def push(self, node, index):
        self._nodeStack.append( (node, index))

    def process(self, csvRecord ):
        key=csvRecord[0]
        index=csvRecord[1]

        newNode=StructureNode(key)
        
        # search for the parent node on the stack
        while self._nodeStack and not index.startswith(self.top()[1] ):
            self._nodeStack.pop()
            
        if not self._nodeStack:
            #new node is top-level
            self._structure.root.add(newNode)
        else:
            # new node is child of top of the stack
            self.top()[0].add(newNode)                
        
        # Update current node state
        self.push(newNode, index)
        

def readStructureCSV(csvfile):
    '''
        Expected CSV record structure:
        <JIRA KEY>,<INDEX>
    '''
    reader= csv.reader(csvfile, delimiter=',', quotechar='"')
    b=StructureBuilder()
    for rec in reader:
        b.process(rec)
    return b.getResult()


def readJiraXml(xmlfile):
    issuesSet= IssuesSet()
    dom=xml.dom.minidom.parse(xmlfile)
    
    for item in dom.getElementsByTagName("item"):
        key=_getElementText(item, "key")
        issType=_getElementText(item, "type")
        summary=_getElementText(item, "summary")
        link=_getElementText(item, "link")

        issue=Issue(key, link, issType, summary)
        
        subtasks=_getFirstElement(item, "subtasks")
        if subtasks<>None:
            for st in subtasks.getElementsByTagName("subtask"):
                stKey=_getText(st)
                issue.subtasks.append(stKey)
        
        issuesSet.add(issue)
    
    return issuesSet
    
def _getFirstElement(root, tag):
    '''
    First child element with given tag, or None
    '''
    elems=root.getElementsByTagName(tag)
    return elems[0] if elems.length>0 else None
    
    
    
def _getElementText(root, tag):
    elem=_getFirstElement(root, tag)
    return _getText(elem) if elem<>None else None

def _getText(elem):
    '''
    Returns the first text child node of elem
    '''
    txt=next( (n for n in elem.childNodes if n.nodeType==Node.TEXT_NODE), None)
    return txt.data if txt<>None else None
    
    

def extendStructureWithSubtasks(structure, issueSet):
    '''
    extends a given structure with subtasks defined in issue descriptor 
    '''
    for iss in issueSet.issues.itervalues():
        for st in iss.subtasks:
            addToStructure(structure, iss.key, st)
        

def addToStructure(structure, parentKey, childKey):
    '''
    No change occurs if
    - parent not found in structure 
    - child with the same childKey already exists
    '''
    parent=structure.find(parentKey)
    if parent==None:
        #cannot find parent - skip
        pass
    else:
        # check if child already exists
        if(not [ch for ch in parent.children if ch.key==childKey]):
            # add child
            parent.add(StructureNode(childKey))
            
            

