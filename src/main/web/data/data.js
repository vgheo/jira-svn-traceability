var data = {
  "issueToCode": [
    {
      "code": {
        "paths": [
          "/branches/project5/jira.json",
          "/trunk/example1/jira.json"
        ],
        "revisions": [
          1,
          9
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
    },
    {
      "comment": "PRJ-10000 unmapped",
      "id": 11,
      "issue": "PRJ-10000",
      "paths": [
        "/branches/project5"
      ]
    },
    {
      "comment": "PRO-O some work ",
      "id": 15,
      "issue": null,
      "paths": [
        "/branches/project5",
        "/branches/project5/jira.json",
        "/branches/project5/report-alt2.html"
      ]
    },
    {
      "comment": "PRO-3 commit",
      "id": 12,
      "issue": "PRO-3",
      "paths": [
        "/branches/.gitignore",
        "/branches/project5",
        "/branches/project5/jira.json"
      ]
    }
  ]
}