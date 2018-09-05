from get_git.utils import make_request

BB_URL='https://api.bitbucket.org/2.0/users/bitbucket/repositories'

class BitbucketClient:
    def __init__(self, username):
        self.username = username

    def get_data(self):
        resp = make_request(BB_URL)
        repos = resp['values']
        while resp.get('next'):
            next_page = make_request(resp['next'])
            repos.extend(next_page['values'])
            resp['next'] = next_page.get('next')
        return repos

