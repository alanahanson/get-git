# get_git
Get user information from Github and Bitbucket profiles

## TO RUN

have docker installed
run the runner in your terminal (./runner)


## TO RUN TESTS

install pip, install pytest, run tests


GH
The user profile should include following information (when avaialble):
total number of public repos (seperate by original repos vs forked repos)
- GET /users/:username/repos
total watcher/follower count
total number of stars recieved
total number of stars given
  - GET /users/:username/starred (array)
total number of open issues
total number of commits to their repos (not forks)
total size of their accounts
a list/count of langagues used
a list/count of repo topics



BB
The user profile should include following information (when avaialble):
total number of public repos (seperate by original repos vs forked repos)
total watcher/follower count
total number of stars recieved
total number of stars given
total number of open issues
total number of commits to their repos (not forks)
total size of their accounts
a list/count of langagues used
a list/count of repo topics
