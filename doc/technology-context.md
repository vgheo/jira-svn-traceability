
- JSON as serialization format
- python as batch processing 
- js - alternative for batch processing
- html/js - view technology
- mustache.js - logicless templates
- angularjs - alternative for rendeing (heavier)

## JIRA

### xml results
XML sample:
https://jira.atlassian.com/sr/jira.issueviews:searchrequest-xml/temp/SearchRequest.xml?jqlQuery=project+%3D+JSWCLOUD+AND+resolution+%3D+Unresolved+and+createdDate+%3E%3D+2018-02-01+ORDER+BY+key+DESC&tempMax=1000


### S-JQL
roots = issue in structure(${structureName}, 'root' )
children = issue in structure(${structureName}, 'parent in ${ISS}'  )


## JIRA pyhton
https://jira.readthedocs.io/en/master/

## JIRA Structure
https://wiki.almworks.com/display/structure/S-JQL+Cookbook

# SVN
## svn python
https://pypi.python.org/pypi/svn

### svn xml log
sample:
svn log --xml --verbose https://github.com/vgheo/jira-svn-traceability.git


# view technology

### mustache
logicless templates
https://github.com/janl/mustache.js/

### bootstrap
https://getbootstrap.com/docs/4.0/getting-started/download/
