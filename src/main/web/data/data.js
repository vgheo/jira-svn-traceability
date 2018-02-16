var data = {
  "issueToCode": [
    {
      "issue": {
        "summary": "f1",
        "key": "PRJ-1",
        "type": "Feature",
        "url": "https://jira.atlassian.com/browse/PRJ-1"
      },
      "code": {
        "paths": [
          "/trunk/example1/jira.json"
        ],
        "revisions": [
          1
        ]
      },
      "level": 0
    },
    {
      "issue": {
        "summary": "s2",
        "key": "PRJ-2",
        "type": "Story",
        "url": "https://jira.atlassian.com/browse/PRJ-2"
      },
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
      "level": 1
    }
  ],
  "unmappedCode": [
    {
      "id": 4,
      "comment": "PRJ-999 unmapped",
      "issue": "PRJ-999",
      "paths": [
        "/trunk/example1"
      ]
    }
  ]
}