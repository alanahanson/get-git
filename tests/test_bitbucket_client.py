from unittest.mock import patch

from get_git.bitbucket_client import BitbucketClient

mock_response = {
    'values': [1,2,3,4,5],
    'next': False,
}
@patch('get_git.bitbucket_client.make_request')
def test_client_makes_request(m_request):
    m_request.return_value = mock_response
    client = BitbucketClient('baz')
    client.get_data()
    assert m_request.called


@patch('get_git.bitbucket_client.make_request')
def test_client_returns_list_of_repos(m_request):
    m_request.return_value = mock_response
    client = BitbucketClient('baz')
    assert client.get_data() == [1,2,3,4,5]
