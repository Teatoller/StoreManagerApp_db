import re
from flask import Flask, jsonify, request, Response, make_response
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_identity,
                                create_access_token, create_refresh_token,
                                jwt_refresh_token_required, get_raw_jwt)
from app.api.v2.models.users import UserModel
from flask_restful import Resource
from db import db_connection
import json
from werkzeug.security import check_password_hash
import datetime
# from app.__init__ import jwt
from app.__init__ import blacklist

blacklist = set()


class Signup(Resource):
    @jwt_required
    def post(self):
        user_detail = UserModel().get_by_username(get_jwt_identity())
        if user_detail['role'] == "user":
            return{'msg': 'not authorised access denied'}, 401

        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']

        valid_username = "".join(data['username'].split())

        if len(valid_username) < 6:
            invalidUsernameErrorMsg = {
                "error": "Invalid username passed in request",
                "helpString": "Username less than six char, sample {'username': 'steven'}"
            }
            response = Response(json.dumps(
                invalidUsernameErrorMsg), status=400, mimetype='application/json')
            return response

        username = data['username']

        if not re.match("^[a-zA-Z0-9_]*$", username):
            invalidUsernameErrorMsg = {
                "error": "Invalid username passed in request",
                "helpString": "Sample, no special char e.g #*& {'username': 'steven'}"
            }
            response = Response(json.dumps(
                invalidUsernameErrorMsg), status=400, mimetype='application/json')
            return response

        email = data['email']
        if not re.match(r"^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$", email):
            invalidEmailErrorMsg = {
                "error": "Invalid email passed in request",
                "helpString": "Email must have @ character {'email': 'Jessica@storeapp.co.ke'}"
            }
            response = Response(json.dumps(invalidEmailErrorMsg),
                                status=400, mimetype='application/json')
            return response

        password = data['password']
        if not re.match("^[a-zA-Z0-9_]*$", password):
            invalidpasswordErrorMsg = {
                "error": "Password cannot be blank or have special characters",
                "helpString": "Enter password, sample {'password': 'test123'}"
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

        current_user = UserModel()
        user = current_user.get_by_username(username)

        if user:
            if check_password_hash(user['password'], password):
                exp = datetime.timedelta(minutes=30)
                access_token = create_access_token(identity=username)
                print(access_token)
                return make_response(jsonify(access_token=access_token), 200)
            return{'msg': 'wrong password'}
        if not user:
            invalidUserErrorMsg = {
                "error": "You are not registered",
                "helpString": "See your system admin for registration"
            }
            response = Response(json.dumps(invalidUserErrorMsg),
                                status=400, mimetype='application/json')
            return response


class Logout(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        if current_user is None:
            return{'msg': 'login to access resource'}, 400

        jti = get_raw_jwt()['jti']
        print(blacklist)
        blacklist.add(jti)
        print(blacklist)
        return jsonify({'message': 'User logout successful'}, 200)
