from get_git.utils import make_request


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
        # this one can take a while - commenting it out so code can run
        # resp = make_request(self.data['links']['commits']['href'])
        # count = len(resp['values'])
        # while resp.get('next'):
        #     next_page = make_request(resp['next'])
        #     count += len(next_page['values'])
        #     resp['next'] = next_page.get('next')
        # return count
        return 0
