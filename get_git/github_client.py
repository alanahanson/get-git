import os

from get_git.utils import make_request

GH_URL = 'https://api.github.com/graphql'
TOKEN=os.environ.get('GH_API_TOKEN')

class GithubClient:
    def __init__(self, username):
        self.username = username

    def get_user(self):
        query =  """
          {user(login:"%s") {
              starredRepositories { totalCount }
              followers { totalCount }
              repositories(first:100) {
                  totalDiskUsage
                  totalCount
                  pageInfo { hasNextPage, endCursor }
                  nodes {
                    id
                    name
                    isFork
                    primaryLanguage { name }
                    issues(states:OPEN) { totalCount }
                    commitComments { totalCount }
                    watchers { totalCount }
                    stargazers { totalCount }
                    languages(first:100) {
                      totalCount
                      pageInfo { hasNextPage, endCursor }
                      nodes { name }
                    }
                    repositoryTopics(first:100) {
                      totalCount
                      pageInfo { hasNextPage, endCursor }
                      nodes {
                        topic { name }
                      }
                    }
                  }
                }
              }
            }
        """ % (self.username)
        return make_request(GH_URL, 'post', token=TOKEN, data=query)

    def _get_additional_repos(self, cursor=None):
        query =  """
          {user(login:"%s") {
              repositories(first:100%s) {
                pageInfo { hasNextPage, endCursor }
                nodes {
                  id
                  name
                  isFork
                  primaryLanguage { name }
                  issues(states:OPEN) { totalCount }
                  commitComments { totalCount }
                  watchers { totalCount }
                  stargazers { totalCount }
                  repositoryTopics(first:100) {
                    totalCount
                    pageInfo { hasNextPage, endCursor }
                    nodes {
                      topic { name }
                    }
                  }
                }
              }
            }
          }
        """ % (self.username, self._add_cursor(cursor))
        return make_request(GH_URL, 'post', token=TOKEN, data=query)

    def _get_additional_topics(self, repo_name, cursor=None):
        query =  """
          {repository(owner:"%s", name:"%s") {
              repositoryTopics(first:100%s) {
                pageInfo { hasNextPage, endCursor }
                nodes {
                  topic { name }
                }
              }
            }
          }
        """ % (self.username, repo_name, self._add_cursor(cursor))
        return make_request(GH_URL, 'post', token=TOKEN, data=query)

    def _add_cursor(self, cursor):
      if cursor:
          return f',after:"{cursor}"'
      return ''

    def _get_all_repos(self, repo_data):
        repos = repo_data['nodes']
        while repo_data['pageInfo']['hasNextPage']:
            cursor = repo_data['pageInfo']['endCursor']
            next_page = self._get_additional_repos(cursor=cursor)
            repos.extend(next_page['data']['user']['repositories']['nodes'])
            repo_data['pageInfo'] = next_page['data']['user']['repositories']['pageInfo']
        return repos

    def _get_all_topics(self, topic_data):
        topics = topic_data['nodes']
        while topic_data['pageInfo']['hasNextPage']:
            cursor = topic_data['pageInfo']['endCursor']
            next_page = self.get_additional_topics(repo['name'], cursor)
            topics.extend(next_page['data']['repository']['repositoryTopics'])
            topic_data['pageInfo'] = next_page['data']['repository']['repositoryTopics']['pageInfo']
        return topics

    def get_data(self):
        result = self.get_user()['data']['user']
        result['repositories']['nodes'] = self._get_all_repos(result['repositories'])

        for repo in result['repositories']['nodes']:
            if repo['repositoryTopics']['totalCount']:
                repo['repositoryTopics']['nodes'] = self._get_all_topics(repo['repositoryTopics'])

        return result
