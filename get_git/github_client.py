from get_git.graphql_gh import GithubGraphqlClient

class GithubProfile:
    def __init__(self, username):
        self.username = username
        self.data = GithubGraphqlClient(username).get_data()
        self.repos = self.data['repositories']['nodes']

    def repo_count(self):
        return {
            'total': self.data['repositories']['totalCount'],
            'forks': len([r for r in self.repos if r['isFork']]),
        }

    def follower_count(self):
        return self.data['followers']['totalCount']

    def watcher_count(self):
        pass
        # a repo has watchers!

    # def watching_count(self):
    #     return self.data['watching']['totalCount']

    # def following_count(self):
    #     return self.data['following']['totalCount']

    def stars_received(self):
        return sum([r['stargazers']['totalCount'] for r in self.repos])

    def stars_given(self):
        return self.data['starredRepositories']['totalCount']

    def open_issues_count(self):
        return sum([r['issues']['totalCount'] for r in self.repos])

    def total_commits(self):
        # this should be commits to user's repos, not forks
        return sum([r['commitComments']['totalCount'] for r in self.repos])

    def account_size(self):
        return self.repos['totalDiskUsage']

    def languages_count(self):
        return len(self.languages_used())

    def languages_used(self):
      s = set()
      [[s.add(node['name']) for node in repo['languages']['nodes']] for repo in self.repos]
      return s
      # any way to flatten that nested comprehension and wrap it with set()?
      # maybe make this an attr in case it needs to be called more than once

    def repo_topics(self):
        pass # TODO

profile = GithubProfile('octocat')
print(profile.stars_received())
