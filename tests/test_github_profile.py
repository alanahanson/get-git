from unittest.mock import patch
from get_git.github_profile import GithubProfile


mock_response = {
    'starredRepositories': { 'totalCount': 10 },
    'followers': { 'totalCount': 20 },
    'repositories': {
        'totalDiskUsage': 52,
        'totalCount': 250,
        'nodes': [{
            'id': 3,
            'name': 'hi',
            'isFork': False,
            'primaryLanguage': {'name': 'Ruby'},
            'issues': {'totalCount': 5 },
            'commitComments': { 'totalCount': 4 },
            'watchers': { 'totalCount': 42 },
            'stargazers': { 'totalCount': 14 },
            'repositoryTopics': {
                'totalCount': 1,
                'nodes': [{'topic': {'name': 'computers'}}],
            },
        }]
    },
}


@patch('get_git.github_profile.GithubClient')
def test_init_calls_github_client(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert m_client.called


@patch('get_git.github_profile.GithubClient')
def test_total_watchers_returns_watchers(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert profile.total_watchers() == 42


@patch('get_git.github_profile.GithubClient')
def test_total_open_issues_returns_open_issues(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert profile.total_open_issues() == 5


@patch('get_git.github_profile.GithubClient')
def test_total_repos_returns_repos(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert profile.total_repos() == 250


@patch('get_git.github_profile.GithubClient')
def test_total_forks_returns_forks(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert profile.total_forks() == 0


@patch('get_git.github_profile.GithubClient')
def test_total_followers_returns_followers(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert profile.total_followers() == 20


@patch('get_git.github_profile.GithubClient')
def test_total_commits_returns_commits(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert profile.total_commits() == 4


@patch('get_git.github_profile.GithubClient')
def test_stars_given_returns_stars_given(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert profile.stars_given() == 10


@patch('get_git.github_profile.GithubClient')
def test_stars_received_returns_stars_received(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert profile.stars_received() == 14


@patch('get_git.github_profile.GithubClient')
def test_repo_topics_returns_repo_topics(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert profile.repo_topics() == [['computers']]


@patch('get_git.github_profile.GithubClient')
def test_account_size_returns_account_size(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert profile.account_size() == 52


@patch('get_git.github_profile.GithubClient')
def test_languages_used_returns_languages_used(m_client):
    m_client.return_value.get_data.return_value = mock_response
    profile = GithubProfile('whatever')
    assert profile.languages_used() == ['Ruby']


