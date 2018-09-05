class UserProfile:
    def __init__(self, data):
        self.gh_name = data.get('github')
        self.bb_name = data.get('bitbucket')

    @property
    def merged_profile(self):
        return {'user': 'lana'}
