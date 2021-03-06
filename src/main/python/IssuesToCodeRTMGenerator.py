'''
Created on Feb 10, 2018

@author: vlad
'''

from domain import Issue, StructureNode, ChangeList, Change  


class IssuesToCodeRTMGenerator:
    '''
    Generated report includes only issues in the issueStructure down to
    the specified leafIssueType.
    
    The Code section is produced only for the deepest issues that are 
    included in the report.
    
    Changed Paths are collected from all child issues.
    Changed Paths are sorted alphabetically.
    
    Report structure:
    
    Example
    - leafIssueType="Feature"
    
    [
        {
            "level" : 0
            "issue" : {
                "key" : "PRJ-1"
                "type" : "Capability"
                "summary" : "cap1" 
            }
        },
        {
            "level" : 1
            "issue" : {
                "key" : "PRJ-2"
                "type" : "Feature"
                "summary" : "feat2" 
            },
            
            "code" : {
                "paths": [
                    "/dir1/file1",
                    "/dir2/file2"
                ]
            }
        }
    ]
    
    '''

    def __init__(self, issueStructure, issueSet, changeList):
        self._issueStructure = issueStructure
        self._issueSet = issueSet
        self._changeList=changeList
        # issue to change map
        self._issueToChangeMap = {}
        for change in changeList.entries:
            if change.issue in self._issueToChangeMap:
                self._issueToChangeMap[change.issue].append(change)
            else:
                self._issueToChangeMap[change.issue]=[change]

    
    def generate(self, leafIssueType):
        '''
        @param leafIssueType: the deepest structure node included in the report
        @param outStream output stream
        @return report model
        '''
        issueToCode = []
        for node in self._issueStructure.root.children:
            issueToCode.extend(self.generateNode(0, node, leafIssueType))

        unmappedCode = self.generateUnmappedCode()
            
        return { "issueToCode" : issueToCode, "unmappedCode" : unmappedCode }
    
        
    def generateNode(self, level, node, leafIssueType):
        ''' 
        Generates a report fragment for a given node.
        @param level current level of the node in the issue structure
        @param node
        @return list of report entries
        
        '''
        issue=self._issueSet.get(node.key);
        
        result=[]
        result.append(self.generateNodeEntry(level, node, leafIssueType))
        
        if issue.type==leafIssueType:
            # stop recursion
            pass
        else:
            # descend to children issues
            for childNode in node.children:
                result.extend(self.generateNode(level+1, childNode, leafIssueType))
        
        return result

    
    def generateNodeEntry(self, level, node, leafIssueType):
        '''
        Generates a report entry for the given node
        @return report entry
        '''
        issue=self._issueSet.get(node.key);
    
        entry = { 
            "level": level,
            "issue" : {
                "key" : issue.key,
                "type" : issue.type,
                "summary" : issue.summary,
                "url" : issue.url 
            }
        }
        
        # generate code link section
        # recursive mapping only for leaf nodes
        recursiveCodeMapping = issue.type==leafIssueType
        entry["code"] = self.generateCodeSection(node, recursiveCodeMapping)
        
        return entry


    def generateCodeSection(self, node, recurse=True):
                
        # recursive: set of keys for current node and all descendants
        # non-recursive : only for current node
        issueScope = [ n.key for n in  [node] + node.allChildren() ] if recurse else [node.key] 
        
        # set of changes that trace to one of the issues in scope
        relatedChanges = set()
        for issueKey in issueScope:
            relatedChanges.update( self._issueToChangeMap.get(issueKey, []) )
    
        code={}

        # all paths, trim base directory, sort
        fullPaths=set( [ p for c in relatedChanges for p in c.paths ])
        code["paths"]=[removePrefix(self._changeList.basePath, p) for p in sorted(fullPaths) ]
        code["revisions"]=sorted(set([c.id for c in relatedChanges ]))
    
        return code
    
    def generateUnmappedCode(self):
        '''
        List of changes that have no issue in the defiend scope 
        '''
        
        issueScopeKeys= set( (n.key for n in self._issueStructure.root.allChildren()) )

        unmappedCode=[ change for change in self._changeList.entries if not change.issue in issueScopeKeys ]
        
        def toJson(change):
            return {"id" : change.id, 
                    "comment" : change.comment,
                    "paths" : change.paths,
                    "issue" : change.issue 
                    }
        
        return [ toJson(change) for change in unmappedCode ]
       

        
    
def removePrefix(prefix, s):
    return s[len(prefix):] if s.startswith(prefix) else s

        

