# get_git
Get merged user information from Github and Bitbucket profiles

## To run the app

Prerequisites:
- have Docker installed
- export relevant env variables to your environment (GH_API_TOKEN, PYTHONPATH)

Run the runner file in your terminal with `./runner`

Go to `http://localhost:4000/user?github={username}&bitbucket={username}` for a JSON response

## To run tests
- `pip install pytest`
- `pytest tests/`

