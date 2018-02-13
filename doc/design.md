


# interfaces

## SVN log
Input

format : XML

svn --xml --verbose

We also need the chagned paths.
We assume that the comment for each revision starts with the JIRA key of the associated issue.

## JIRA structure
Export from JIRA structure view.
- Excel > CSV

ID,Index


# Domain model


IssueSet {
	issueMap : Map(String, Issue)
	jiraURL: String
	projectId : String	
}

Constraint: all issues contained in the same set are from the same jira project
- the key is formed as projectId + '-' + issueNo


Issue {
	key : String
	type : String
	summary : String
}


```
issueSet = {	
	issueMap = {
		"ID-1" : Issue("ID-1", "feature", "sss sss"),
		"ID-2" : Issue("ID-2", "story", "s2"),
		...
	}
}
```

Structure:

Node {
	issueKey : String
	children : List(Node)
}


```
structure = [
	Node( "ID-1", [
		Node("ID-2", [
			Node("ID-3")
		])
	])
]
```

Svn log :

class SvnLog {
	baseURL : String
	entries : List(LogEntry)
}

class SvnLogEntry {
	revision: Integer
	comment: String
	paths : List(String)
	branch : String
	issues : List(String)
}



## Open points
-  For multiple IssueSets (from different projects) - issue mapping based on key alone 
assumes that all issues in the same set share the same key prefix (eg "PRJ-") 



# Transforms

## SVN-xml to SvnLog

## release

# Main flow



