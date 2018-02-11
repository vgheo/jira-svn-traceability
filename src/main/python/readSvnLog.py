'''
Created on Feb 10, 2018

@author: vlad
'''
from domain import ChangeList, Change


def readSvnLogXml(xmlfile):
    # TODO
    return mockLog()


def mockLog():
    chList=ChangeList("/")
    
    chList.add(Change(1, "PRJ-2 comm", ["/a.txt"], "PRJ-2" ))
    chList.add(Change(2, "PRJ-3 comm", ["/b.txt"], "PRJ-3" ))
            
    return chList