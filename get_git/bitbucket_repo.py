from utils.make_request import make_request


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
        # TODO: update this - inaccurate data/inconsistent response
        if data.get('has_issues'):
            try:
                resp = make_request(self.data['links']['issues']['href'])
                return resp['size']
            except RequestException:
                return 0
        return 0

