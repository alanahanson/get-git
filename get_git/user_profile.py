from get_git.bitbucket_profile import BitbucketProfile
from get_git.github_profile import GithubProfile


class UserProfile:
    def __init__(self, data):
        self.gh_name = data.get('github')
        self.bb_name = data.get('bitbucket')

    @property
    def merged_profile(self):
        if None in [self.gh_name, self.bb_name]:
            return {'error': 'Must provide usernames for Github and Bitbucket.'}
        return {
            'github_user': self.gh_name,
            'bitbucket_user': self.bb_name,
            'data': self._merge_data()
        }

    def _merge_data(self):
        gh = GithubProfile(self.gh_name)
        bb = BitbucketProfile(self.bb_name)

        data = {}

        data['languages_used'] = self._language_data(gh.languages_used(), bb.languages_used())

        forks = self._sum_values(gh.total_forks(), bb.total_forks())
        total = self._sum_values(gh.total_repos(), bb.total_repos())
        data['repos'] = {
            'total': total,
            'forks': forks,
            'original': total - forks,
        }

        data['account_size'] = self._sum_values(gh.account_size(), bb.account_size())
        data['total_watchers'] = self._sum_values(gh.total_watchers(), bb.total_watchers())
        data['total_commits'] = self._sum_values(gh.total_commits(), bb.total_commits())

        data['gh_only'] = {}
        data['gh_only']['total_open_issues'] = gh.total_open_issues()
        data['gh_only']['total_followers'] = gh.total_followers()
        data['gh_only']['stars_given'] = gh.stars_given()
        data['gh_only']['stars_received'] = gh.stars_received()
        data['gh_only']['repo_topics'] = {'count': len(gh.repo_topics()), 'topics': gh.repo_topics()}
        return data

    def _language_data(self, lang1, lang2):
        l = lang1
        l.extend(lang2)
        l = list(set(l))
        return {'count': len(l), 'languages': l}

    def _sum_values(self, x, y):
        return sum([num for num in [x,y] if num])
