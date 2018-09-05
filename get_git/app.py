from flask import Flask, jsonify, request

from get_git.user_profile import UserProfile


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¯\_(ツ)_/¯'

@app.route('/user', methods=['GET'])
def show_user_profile():
    data = {
        'bitbucket': request.args.get('bitbucket'),
        'github': request.args.get('github')
    }
    # user = UserProfile(data)
    user = {'a': 'alana'}
    response = jsonify(user)
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
