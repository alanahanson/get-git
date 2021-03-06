from flask import Flask, jsonify, request

from get_git.user_profile import UserProfile


app = Flask(__name__)

@app.route('/user', methods=['GET'])
def show_user_profile():
    data = {
        'bitbucket': request.args.get('bitbucket'),
        'github': request.args.get('github')
    }
    user = UserProfile(data)
    response = jsonify(user.merged_profile)
    response.status_code = 200
    return response


