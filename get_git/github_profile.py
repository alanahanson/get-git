from get_git.github_client import GithubClient

from get_git.github_repo import GithubRepo

class GithubProfile:
    def __init__(self, username):
        self.data = self._get_data(username)
        self.repos = self._get_repos()

    def _get_data(self, username):
        return GithubClient(username).get_data()

    def _get_repos(self):
        return [GithubRepo(node) for node in self.data['repositories']['nodes']]

    def total_watchers(self):
        return sum([r.watcher_count for r in self.repos])

    def total_open_issues(self):
        return sum([r.issues_count for r in self.repos])

    def total_repos(self):
        self.data['repositories']['totalCount']

    def total_forks(self):
        return len(r for r in self.repos if r.is_fork)

    def total_followers(self):
        return self.data['followers']['totalCount']

    def languages_used(self):
        return {r.language for r in self.repos}

    def languages_count(self):
        return len(self.languages_used())

    def account_size(self):
        return self.data['repositories']['totalDiskUsage']
    def total_commits(self):
        return sum([r.commits_count for r in self.repos])

    def repo_topics(self):
        return [r.topics for r in self.repos]

    def stars_given(self):
        return self.data['starredRepositories']['totalCount']

    def stars_received(self):
        return sum([r.stars_count for r in self.repos])


profile = GithubProfile('octocat')
print(profile.stars_received())
