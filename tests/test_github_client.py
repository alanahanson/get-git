# from unittest import mock

# from get_git.github_client import GithubClient


# class FakeResponse:
#     def __init__(self, json_data, status_code):
#         self.json_data = json_data
#         self.status_code = status_code

# mock_user_data = {
#     'login': 'alanahanson',
#     'id': 7280332,
#     'public_repos': 14,
#     'public_gists': 9,
#     'followers': 5,
#     'following': 0,
# }

# @mock.patch('github_client.GithubClient._user')
# @mock.patch('github_client.GithubClient._repos')
# def test_follower_count():
#     g =
