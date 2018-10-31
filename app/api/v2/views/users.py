import re
from flask import Flask, jsonify, request, Response, make_response
from flask_jwt_extended import(
    JWTManager, jwt_optional, create_access_token, get_jwt_identity)
from app.api.v2.models.users import UserModel
from flask_restful import Resource
from db import db_connection
import json
from werkzeug.security import check_password_hash


class Signup(Resource):
    def post(self):
        data = request.get_json()
        first_name = data['firstname']
        last_name = data['lastname']

        valid_username = "".join(data['username'].split())

        if len(valid_username) < 6:
            invalidUsernameErrorMsg = {
                "error": "Invalid username passed in request",
                "helpString": "Username less than six char data to be passed similar to this {'username': 'steven'}"
            }
            response = Response(json.dumps(
                invalidUsernameErrorMsg), status=400, mimetype='application/json')
            return response

        user_name = data['username']

        if not re.match("^[a-zA-Z0-9_]*$", user_name):
            invalidUsernameErrorMsg = {
                "error": "Invalid username passed in request",
                "helpString": "Username cannot have special characters e.g # * & data to be passed similar to this {'username': 'steven'}"
            }
            response = Response(json.dumps(
                invalidUsernameErrorMsg), status=400, mimetype='application/json')
            return response

        email = data['email']
        if not re.match(r"^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$", email):
            invalidEmailErrorMsg = {
                "error": "Invalid email passed in request",
                "helpString": "Email must have @ characters, data to be passed similar to this {'email': 'Jessica@storeapp.co.ke'}"
            }
            response = Response(json.dumps(invalidEmailErrorMsg),
                                status=400, mimetype='application/json')
            return response

        password = data['password']
        if not re.match("^[a-zA-Z0-9_]*$", password):
            invalidpasswordErrorMsg = {
                "error": "Password cannot be blank or have special characters",
                "helpString": "Enter start password , data to be passed similar this {'password': 'test123'}"
            }
            response = Response(json.dumps(
                invalidpasswordErrorMsg), status=400, mimetype='application/json')
            return response

        role = data['role']

        user = UserModel(
            data['firstname'],
            data['lastname'],
            data['username'],
            data['email'],
            data['password'],
            data['role']
        )
        user.saveuser()
        return make_response(jsonify(
                {'msg': 'user created succesfully'}), 201)


class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

#  validate user input
        if not username:
            return {'message': 'username cannot be empty'}, 400

        if not password:
            return {'message': 'password cannot be empty'}, 400
        
        user = UserModel.get_by_username()

        if user:
            if check_password_hash(user['password'], password):
                access_token = create_access_token(identity=username)
                return jsonify(access_token=access_token), 200
        if not user:
            invalidUserErrorMsg = {
                "error": "You are not registered",
                "helpString": "See your system admin for registration"
            }
            response = Response(json.dumps(invalidUserErrorMsg),
                                status=400, mimetype='application/json')
            return response
        

class Logoutaccess(Resource):
    """Docstring revokes current user token """

    def post(self):
        jti = get_raw_jwt()['jti']
        blackedlist.add(jti)
        return jsonify({'message': 'User logout successful'}), 200


class Logoutrefresh(Resource):
    """Docstring prevents use of blacklisted tokens """

    def delete(self):
        jti = get_raw_jwt()['jti']
        blackedlist.add(jti)
        return jsonify({'message': 'User logout successful'}), 200
