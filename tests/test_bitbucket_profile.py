from unittest.mock import patch
from get_git.bitbucket_profile import BitbucketProfile
from get_git.bitbucket_repo import BitbucketRepo


mock_response = [
    {
        'size': 2,
        'parent': True,
        'language': 'Python',
        'links': {
            'commits': {'href': 'click_me'},
            'watchers': {'href': 'a_url'}
        }
    },
    {
        'size': 3,
        'language': 'Ruby',
        'links': {
            'commits': {'href': 'click_me'},
            'watchers': {'href': 'a_url'}
        }
    },
    {
        'size': 1,
        'language': 'Python',
        'links': {
            'commits': {'href': 'click_me'},
            'watchers': {'href': 'a_url'}
        }
    }
]


@patch('get_git.bitbucket_profile.BitbucketClient')
def test_init_calls_bitbucket_client(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = BitbucketProfile('foo')
    assert m_client.called


@patch('get_git.bitbucket_repo.make_request')
@patch('get_git.bitbucket_profile.BitbucketClient')
def test_total_watchers_returns_watchers(m_client, m_request):
    m_request.return_value = {'size': 10}
    m_client.return_value.get_data.return_value = mock_response
    profile = BitbucketProfile('foo')
    assert profile.total_watchers() == 30


@patch('get_git.bitbucket_profile.BitbucketClient')
def test_total_open_issues_returns_none(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = BitbucketProfile('foo')
    assert profile.total_open_issues() == None


@patch('get_git.bitbucket_profile.BitbucketClient')
def test_total_repos_returns_repos(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = BitbucketProfile('foo')
    assert profile.total_repos() == 3


@patch('get_git.bitbucket_profile.BitbucketClient')
def test_total_forks_returns_forks(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = BitbucketProfile('foo')
    assert profile.total_forks() == 1


@patch('get_git.bitbucket_profile.BitbucketClient')
def test_total_followers_returns_none(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = BitbucketProfile('foo')
    assert profile.total_followers() == None


# @patch('get_git.bitbucket_profile.BitbucketClient')
# def test_total_commits_returns_commits(m_client):
#     m_client.return_value.get_data.return_value = mock_response
#     profile = BitbucketProfile('foo')
#     assert profile.total_commits() == 3


@patch('get_git.bitbucket_profile.BitbucketClient')
def test_stars_given_returns_none(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = BitbucketProfile('foo')
    assert profile.stars_given() == None


@patch('get_git.bitbucket_profile.BitbucketClient')
def test_stars_received_returns_none(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = BitbucketProfile('foo')
    assert profile.stars_received() == None


@patch('get_git.bitbucket_profile.BitbucketClient')
def test_repo_topics_returns_none(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = BitbucketProfile('foo')
    assert profile.repo_topics() == None


@patch('get_git.bitbucket_profile.BitbucketClient')
def test_account_size_returns_account_size(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = BitbucketProfile('foo')
    assert profile.account_size() == 6


@patch('get_git.bitbucket_profile.BitbucketClient')
def test_languages_used_returns_languages_used(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = BitbucketProfile('foo')
    assert 'Ruby' in profile.languages_used()
    assert 'Python' in profile.languages_used()



