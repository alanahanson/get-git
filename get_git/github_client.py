import os

from utils import make_request

GH_URL = 'https://api.github.com/graphql'
TOKEN=os.environ.get('GH_API_TOKEN')

class GithubClient:
    def __init__(self, username):
        self.username = username

    def get_user(self):
        query =  """
          {user(login:"%s") {
              starredRepositories { totalCount }
              watching { totalCount }
              followers { totalCount }
              following { totalCount }
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

    def get_additional_repos(self, cursor=None):
        query =  """
          {user(login:"%s") {
              repositories(first:100%s) {
                pageInfo { hasNextPage, endCursor }
                nodes {
                  id
                  name
                  isFork
                  languages(first:100) {
                    totalCount
                    pageInfo { hasNextPage, endCursor }
                    nodes { name }
                  }
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

    def get_additional_topics(self, repo_name, cursor=None):
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

    def get_data(self):
        result = self.get_user()['data']['user']
        repos = result['repositories']
            cursor = repos['pageInfo']['endCursor']
            next_page = self.get_additional_repos(cursor=cursor)
            repos['nodes'].extend(next_page['data']['user']['repositories']['nodes'])
            repos['pageInfo'] = next_page['data']['user']['repositories']['pageInfo']

        for repo in repos['nodes']:
            while repo['repositoryTopics']['pageInfo']['hasNextPage']:
                cursor = repo['repositoryTopics']['pageInfo']['endCursor']
                next_page = self.get_additional_topics(repo['name'], cursor)
                repo['repositoryTopics'].extend(next_page['data']['repository']['repositoryTopics'])
        return result
