from get_git.bitbucket_repo import BitbucketRepo
from get_git.bitbucket_client import BitbucketClient


class BitbucketProfile:
    def __init__(self, username):
        self.username = username
        self.data = self._get_data()
        self.repos = self._get_repos()

    def _get_data(self):
        return BitbucketClient(self.username).get_data()

    def _get_repos(self):
        return [BitbucketRepo(node) for node in self.data]

    def total_watchers(self):
        return sum([r.watcher_count for r in self.repos])

    def total_open_issues(self):
        return None

    def total_repos(self):
        return len(self.repos)

    def total_forks(self):
        return len([r for r in self.repos if r.is_fork])

    def total_followers(self):
        # not available for team accounts in version 2.0
        return None

    def languages_used(self):
        return [r.language for r in self.repos]

    def languages_count(self):
        return len(self.languages_used)

    def account_size(self):
        return sum([r.size for r in self.repos])

    def total_commits(self):
        return sum([r.commits_count for r in self.repos])

    def repo_topics(self):
        return None

    def stars_given(self):
        return None

    def stars_received(self):
        return None
