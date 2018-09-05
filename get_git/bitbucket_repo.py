#     'has_issues': False,
#     'links': {
#                  'commits': {   'href': 'https://api.bitbucket.org/2.0/repositories/bitbucket/django-piston/commits'},
#                  'watchers': {   'href': 'https://api.bitbucket.org/2.0/repositories/bitbucket/django-piston/watchers'}},
#     'name': 'django-piston',

def make_request(url, token):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise RequestException(f'Request to {url} failed with status code {response.status_code}.')

class BitbucketRepo:
    def __init__(self, data):
        self.data = data
        self.size = data['size']
        self.is_fork = data.get('parent')
        self.language = data['language']

    @property
    def watcher_count(self):
        resp = make_request(self.data['links']['watchers']['href'])
        return resp['size']

    @property
    def commits_count(self):
        resp = make_request(self.data['links']['commits']['href'])
        count = len(resp['values'])
        while resp.get('next'):
            next_page = make_request(resp['next'])
            commits += len(next_page['values'])
        return count

    @property
    def issues_count(self):
        if data.get('has_issues'):
            try:
                resp = make_request(self.data['links']['issues']['href'])
                return resp['size']
            except RequestException:
                return 0
        return 0

