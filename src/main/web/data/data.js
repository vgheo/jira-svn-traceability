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
        "key": "PRJ-1", 
        "summary": "f1", 
        "type": "Feature", 
        "url": "https://jira.atlassian.com/browse/PRJ-1"
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
        "key": "PRJ-2", 
        "summary": "s2", 
        "type": "Story", 
        "url": "https://jira.atlassian.com/browse/PRJ-2"
      }, 
      "level": 1
    }
  ], 
  "unmappedCode": [
    {
      "comment": "PRJ-999 unmapped", 
      "id": 4, 
      "issue": "PRJ-999", 
      "paths": [
        "/trunk/example1"
      ]
    }
  ]
}