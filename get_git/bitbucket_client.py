import requests

BB_BASE_URL='https://api.bitbucket.org'

class RequestException(Exception):
    pass

# /2.0/users/{username}/followers
def make_request(url):
    headers = {'Authorization': 'Bearer ZfjbDbUS9asa4i6UtgiqB0C5'}
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise RequestException(f'Request to {url} failed with status code {response.status_code}.')

# Path    Methods
# /users/{username}   GET
# /users/{username}/followers GET
# /users/{username}/following GET
# /users/{username}/repositories  GET

class BitbucketProfile:
    def __init__(username):
        self.username = username
        self.repos = self._get_repos()
        # self.follower_count = get_followers()
        # self.following_count = get_following()
        # api does not allow this for a team account?

    def _get_repos(self):
        url = f'{BB_BASE_URL}/2.0/users/bitbucket/repositories'
        resp = make_request(url)
        repos = resp['values']
        while resp.get('next'):
            next_page = make_request(resp['next'])
            repos.extend(next_page['values'])
            resp['next'] = next_page.get('next')
        return [BitbucketRepo(data) for data in repos]

    def total_watchers(self):
        return sum([r.watcher_count for r in self.repos])

    def total_open_issues(self):
        return sum([r.issues_count for r in self.repos])

    def total_repos(self):
        return len(self.repos)

    def total_forks(self):
        return len(r for r in self.repos if r.is_fork)

    def languages_used(self):
        return {r.language for r in self.repos}

    def languages_count(self):
        return len(self.languages_used)

    def account_size(self):
        return sum([r.size for r in self.repos])

    def total_commits(self):
        return sum([r.commits_count for r in self.repos])

    def repo_topics(self):
        return []

    def stars_given(self):
        return 0

    def stars_received(self):
        return 0

    # def follower_count(self):
    #     url = f'{BB_BASE_URL}/2.0/users/{self.username}/followers'
    #     return make_request(url)['count']

