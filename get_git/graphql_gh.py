import requests
import os

class GithubGraphqlClient:
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
                  languages(first:100) {
                    totalCount
                    pageInfo { hasNextPage, endCursor }
                    nodes { name }
                  }
                  issues(states:OPEN) { totalCount }
                  commitComments { totalCount }
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
        """ % (self.username)
        return self.make_request(query)

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
        return self.make_request(query)

    def get_additional_languages(self, repo_name, cursor=None):
        query = """
          {repository(owner:"%s", name:"%s") {
              languages(first:100%s) {
                  pageInfo { hasNextPage, endCursor }
                  nodes { name }
              }
            }
          }
        """ % (self.username, repo_name, add_cursor(cursor))
        return self.make_request(query)

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
        return self.make_request(query)

    def _add_cursor(self, cursor):
      if cursor:
          return f',after:"{cursor}"'
      return ''

    def get_data(self):
        result = self.get_user()['data']['user']
        repos = result['repositories']
        while repos['pageInfo']['hasNextPage']: # returns boolean
            cursor = repos['pageInfo']['endCursor']
            next_page = self.get_additional_repos(cursor=cursor)
            repos['nodes'].extend(next_page['data']['user']['repositories']['nodes'])
            repos['pageInfo'] = next_page['data']['user']['repositories']['pageInfo']

        for repo in repos['nodes']:
            while repo['languages']['pageInfo']['hasNextPage']:
                cursor = repo['languages']['pageInfo']['endCursor']
                next_page = self.get_additional_languages(repo['name'], cursor)
                repo['languages'].extend(next_page['data']['repository']['languages'])

            while repo['repositoryTopics']['pageInfo']['hasNextPage']:
                cursor = repo['repositoryTopics']['pageInfo']['endCursor']
                next_page = self.get_additional_topics(repo['name'], cursor)
                repo['repositoryTopics'].extend(next_page['data']['repository']['repositoryTopics'])
        return result

    def make_request(self, query):
        headers = {"Authorization": f"{os.environ.get('GH_API_TOKEN')}"}
        response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Query failed with status code {response.status_code}. Query: {query}')




