import requests

GH_BASE_URL='https://api.github.com'

class GithubClient:

    def __init__(self, username):
        self.username = username
        self.user = self._user()
        self.repos = self._repos()

    def _user(self):
        return requests.get(f'{GH_BASE_URL}/users/{self.username}').json()

    def _repos(self):
        return requests.get(f'{GH_BASE_URL}/users/{self.username}/repos').json()

    def orig_repo_number(self):
        return len([r for r in self.repos if r['fork']])

    def forks_number(self):
        return len([r for r in self.repos if not r['fork']])

    def follower_count(self):
        return self.user['followers']

    def stars_received(self):
        return sum([r['stargazers_count'] for r in self.repos])

    def stars_given(self):
        return requests.get(f'{GH_BASE_URL}/users/{self.username}/starred')

    def open_issues_count(self):
        return sum([r['open_issues_count'] for r in self.repos])

    def total_commits(self):
        # come back to this one - individual get requests for each repo??? :(
        return

    def account_size(self):
        return sum([r['size'] for r in self.repos])

    def languages_used(self):
        # come back to this one - individual get requests for each repo??? :(
        return

    def repo_topics(self):
        # ????
        return
