import os

import jwt
from flask import Flask, request, jsonify
import re

from flask.views import MethodView
from flask_cors import CORS

from database import Database, User

app = Flask(__name__)
CORS(app)

SECRET_KEY = os.environ.get('SECRET_KEY', '1234')


@app.route('/api/v1/registration', methods=['POST'])
def register():
    """
    @api {POST} /api/v1/registration/ User registration
    @apiVersion 1.0.0

    @apiName PostRegistration
    @apiGroup Authentication

    @apiParam {String="\w"} username User's username.
    @apiParam {String{8..}} password User's password.
    @apiParam {String} email User's email.

    @apiSuccess {String} welcomeMessage Personalised welcome message

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        'welcome message': 'Thank you for joining Cristina23'
    }

    @apiError (Unauthorized 401) {Object} InvalidPassword
    @apiError (Unauthorized 401) {Object} InvalidUsername
    @apiError (Unauthorized 401) {Object} UnavailableUsername
    @apiError (Unauthorized 401) {Object} InvalidEmailFormat
    @apiError (InternalServerError 500) {Object} InternalServerError

    """

    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    try:
        # needs to have one nr,one letter, one non standard char
        # currently matches only if is in this specific order
        password_match = r"^[a-z\d\W]{8,}$"
        invalid_username = r'^[\W]+$'
        email_match = r'([\w\.\-]+)@([\w]+)\.([\w]+){2,}'

        database_instance = Database()
        user = database_instance.get_user_by_name(username)

        # password should be at least 8 char and contain one random nr, letter and special char
        if re.search(password_match, password) is None:
            raise AssertionError('invalid password')

        if not username or re.search(invalid_username, username) is not None:
            raise AssertionError('invalid username')

        if user:
            raise AssertionError('username already taken')

        if not email or not re.fullmatch(email_match, email):
            raise AssertionError('invalid email format')

        database_instance.create_user(username, email, password)
        response = jsonify({'welcome message': f'Thank you for joining {username.capitalize()}'})
        return response

    except AssertionError as a:
        response = jsonify({
            'error': 'Unauthorized',
            'description': str(a)
        })
        response.status_code = 401
        return response

    except:
        response = jsonify({'error': 'unknown error', 'description': 'internal server error'})
        response.status_code = 500
        return response


@app.route('/api/v1/login', methods=['POST'])
def login():
    """
    @api {POST} /api/v1/login/ User login
    @apiVersion 1.0.0

    @apiName PostLogin
    @apiGroup Authentication

    @apiParam {String} username User's username.
    @apiParam {String} password User's password.

    @apiSuccess {String} token User's jwt.

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "token": "eyJ0eXA..."
    }

   @apiError (Unauthorized 401 ) {Object} InvalidLogin Username or password is incorrect.

    """
    username = request.json['username']
    password = request.json['password']

    database_instance = Database()
    user = database_instance.get_user_by_name(username)

    if user and user.password == password:
        token = jwt.encode({'user': username, 'id': user.id}, SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token.decode('ascii')})
    else:
        response = jsonify({'error': 'InvalidLogin', 'description': 'username or password incorrect'})
        response.status_code = 401
        return response


def validate_token(f):
    def _wrapper(*args, **kwargs):

        try:
            auth = request.headers.get('Authorization')
            auth_token = auth.split()[1]
            auth_token_decoded = jwt.decode(auth_token, SECRET_KEY, verify=True)
            user_id = auth_token_decoded['id']

            database_instance = Database()
            user = database_instance.get_user_by_id(user_id)
            kwargs['user'] = user

            return f(*args, **kwargs)

        except:
            response = jsonify({'error': 'unknown error', 'description': 'internal server error'})
            response.status_code = 403
            return response

    return _wrapper


class ProfileView(MethodView):
    @validate_token
    def get(self, user: User = None):
        """
        @api {GET} /api/v1/profile/ Get user information
        @apiVersion 1.0.0

        @apiName GetProfile
        @apiGroup Authentication

        @apiHeader {String} token The users API token in the format "Token {token}".

        @apiParam {String} secret User's secret.


        @apiSuccess {String} secret User's secret.

        @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "secret message": "I like penguins"
        }

        @apiError (InternalServerError 500) {Object} InternalServerError

        """
        try:
            return jsonify({'secret message': user.secret})
        except Exception as e:
            response = jsonify({'error': 'unknown error', 'description': 'internal server error'})
            response.status_code = 500
            return response

    @validate_token
    def patch(self, user: User = None):
        """
        @api {PATCH} /api/v1/profile/ Update user's secret
        @apiVersion 1.0.0

        @apiName PatchProfile
        @apiGroup Authentication

        @apiHeader {String} token The users API token in the format "Token {token}".

        @apiParam {String} new_secret User's secret input.

        @apiSuccess {String} new_secret User's new secret.

        @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
            {
                "updated secret message": "I also like cats"
            }

        @apiError (InternalServerError 500) {Object} InternalServerError

        """
        new_secret = request.json['new_secret']

        try:
            database_instance = Database()
            database_instance.change_user_secret(user.id, new_secret)
            response = jsonify({'updated secret message': new_secret})
            return response
        except Exception as e:
            response = jsonify({'error': 'unknown error', 'description': 'internal server error'})
            response.status_code = 500
            return response

    @validate_token
    def delete(self, user=None):
        """
        @api {DELETE} /api/v1/profile/ Delete user's profile
        @apiVersion 1.0.0

        @apiName DeleteProfile
        @apiGroup Authentication

        @apiHeader {String} token The users API token in the format "Token {token}".

        @apiParam {Number} id User's id.

        @apiSuccess {String} message Profile is deleted.

        @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK {}

        @apiError (InternalServerError 500) {Object} InternalServerError

        """

        try:
            database_instance = Database()
            database_instance.remove_user(user.id)
            response = jsonify({})
            return response
        except Exception as e:
            response = jsonify({'error': 'unknown error', 'description': 'internal server error'})
            response.status_code = 500
            return response


app.add_url_rule('/api/v1/profile', view_func=ProfileView.as_view('myview'))

application = app

if __name__ == '__main__':
    app.run(os.getenv('IP', "0.0.0.0"),
            port=(os.getenv("PORT", "5000")),
            debug=False)
