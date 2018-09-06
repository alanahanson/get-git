from unittest.mock import patch, MagicMock

from get_git.user_profile import UserProfile


def test_returns_error_for_missing_names():
    data = {'github': 'a_name'}
    u = UserProfile(data)
    assert u.merged_profile == {'error': 'Must provide usernames for Github and Bitbucket.'}

@patch('get_git.user_profile.GithubProfile', MagicMock())
@patch('get_git.user_profile.BitbucketProfile', MagicMock())
def test_merge_data_returns_dict():
    u = UserProfile({'github': 'me', 'bitbucket': 'you'})
    resp = u._merge_data()
    assert len(resp.keys()) == 6


