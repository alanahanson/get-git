class GithubRepo:
    def __init__(self, data):
        self.data = data
        self.is_fork = data.get('isFork')
        self.language = data.get('primaryLanguage')

    @property
    def watcher_count(self):
        return self.data['watchers']['totalCount']

    @property
    def commits_count(self):
        return self.data['commitComments']['totalCount']

    @property
    def issues_count(self):
        return self.data['issues']['totalCount']

    @property
    def stars_count(self):
        return self.data['stargazers']['totalCount']

    @property
    def topics(self):
        return [node['topic']['name'] for node in self.data['respositoryTopics']['nodes']]
