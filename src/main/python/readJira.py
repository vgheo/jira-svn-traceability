'''
Created on Feb 10, 2018

@author: vlad
'''


import xml.dom.minidom
from xml.dom.minidom import Node

from domain import IssuesSet, Issue

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
        if subtasks:
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
    return _getText(elem) if elem else None

def _getText(elem):
    '''
    Returns the first text child node of elem
    '''
    txt=next( (n for n in elem.childNodes if n.nodeType==Node.TEXT_NODE), None)
    return txt.data if txt else None

def extendStructureWithSubtasks(structure, issueSet):
    '''
    extends a given structure with subtasks defined in issue descriptor 
    '''
    for iss in issueSet.issues.itervalues():
        for st in iss.subtasks:
            structure.add(iss.key, st)
        


