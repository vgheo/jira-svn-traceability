'''
Created on Feb 16, 2018

@author: vlad
'''
import csv

from domain import Structure, StructureNode

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

