var data = {
  "issueToCode": [
    {
      "code": {
        "paths": [
          "/trunk/example1/jira.json"
        ], 
        "revisions": [
          1
        ]
      }, 
      "issue": {
        "url": "https://jira.atlassian.com/browse/PRJ-1", 
        "type": "Feature", 
        "key": "PRJ-1", 
        "summary": "f1"
      }, 
      "level": 0
    }, 
    {
      "code": {
        "paths": [
          "/trunk/.gitignore", 
          "/trunk/example1", 
          "/trunk/example1/jira.json", 
          "/trunk/example1/report-alt2.html"
        ], 
        "revisions": [
          2, 
          3
        ]
      }, 
      "issue": {
        "url": "https://jira.atlassian.com/browse/PRJ-2", 
        "type": "Story", 
        "key": "PRJ-2", 
        "summary": "s2"
      }, 
      "level": 1
    }
  ], 
  "unmappedCode": [
    {
      "comment": "PRJ-999 unmapped", 
      "paths": [
        "/trunk/example1"
      ], 
      "issue": "PRJ-999", 
      "id": 4
    }
  ]
}