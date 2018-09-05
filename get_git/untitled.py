user(login: "%s")


keys = [('starredRepositories', ['totalCount']),
('watching', ['totalCount']),
('followers', ['totalCount']),
('following', ['totalCount']),
(repo_key, [
    'totalCount',
    'totalDiskUsage',
    {'pageInfo': ['hasNextPage', 'endCursor']},
    {'nodes': [
        'id',
        'name',
        'isFork',
        {lang_key: [
            'totalCount',
            {'pageInfo': ['hasNextPage', 'endCursor']},
            {'nodes': ['name']},
        ]},
        {'issues(states:OPEN)': ['totalCount']},
        {'commitComments': ['totalCount']},
        {'stargazers': ['totalCount']},
        {topics_key: [
            'totalCount',
            {'pageInfo': ['hasNextPage', 'endCursor']},
            {'nodes': [{'topic': ['name']}]},
        ]}
    ]}
])
]

d = {k:v for k, v in keys}

q = {
  'starredRepositories' {
      ['totalCount'],
  },
  'watching' {
      ['totalCount'],
  },
  'followers' {
      ['totalCount'],
  },
  'following' {
      ['totalCount'],
  },
  repo_key {
      [
        'totalDiskUsage',
        'totalCount',
        'pageInfo' {
            ['hasNextPage', 'endCursor'],
        }
        'nodes' {
              'id'
              'name'
              'isFork'
              'languages(first: 100)' {
                'totalCount'
                'pageInfo' {
                  'hasNextPage'
                  'endCursor'
                }
                'nodes' {
                  'name'
                }
              }
              'issues(states:OPEN)' {
                'totalCount'
              }
              'commitComments' {
                'totalCount'
              }
              'stargazers' {
                'totalCount'
              }
              'repositoryTopics(first:100)' {
                'totalCount'
                'pageInfo' {
                  'hasNextPage'
                  'endCursor'
                }
                'nodes' {
                  'topic' {
                    'name'
                  }
