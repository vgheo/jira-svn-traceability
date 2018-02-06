

# requirements

Given
- a JIRA project P, setup with structure plugin
- a svn repository R

REQ1. Generate feature-commit matrix with the format specified in example1/report.html




Next:
- multiple projects
- multiple repos



# technology context

- JSON as serialization format
- python as batch processing 
- js - alternative for batch processing
- html/js - view technology
- mustache.js - logicless templates
- angularjs - alternative for rendeing (heavier)



## JIRA pyhton
https://jira.readthedocs.io/en/master/

## JIRA Structure
https://wiki.almworks.com/display/structure/S-JQL+Cookbook

## svn python
https://pypi.python.org/pypi/svn



# design

## Extract JIRA project structure

This will be run only once.


### S-JQL
roots = issue in structure(${structureName}, 'root' )
children = issue in structure(${structureName}, 'parent in ${ISS}'  )


### ALT1. export form JIRA
https://confluence.atlassian.com/jiracoreserver073/working-with-search-results-861257284.html
- csv
- xml

Q: how to export parent/sub-item relation ?

A: Structure view  > index 
- export excel > csv



### ALT2. use jira-python api

issue: needs security set-up






