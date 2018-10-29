from flask_restful import Resource
from flask import request, Response
import json
from app.api.v1.models.users import UserModel, ListDatabase
import re
from werkzeug.security import generate_password_hash, \
     check_password_hash


class Registration(Resource):
    def post(self):
        data = request.get_json(force=True)
        valid_username = "".join(data['username'].split())

        if len(valid_username) < 6:
            invalidUsernameErrorMsg = {
                "error": "Invalid username passed in request",
                "helpString": "Username less than six char data to be passed similar to this {'username': 'steven'}"
                }
            response = Response(json.dumps(invalidUsernameErrorMsg), status=400, mimetype='application/json')
            return response

        username = data['username']
        
        if not re.match("^[a-zA-Z0-9_]*$", username):
            invalidUsernameErrorMsg = {
                "error": "Invalid username passed in request",
                "helpString": "Username cannot have special characters e.g # * & data to be passed similar to this {'username': 'steven'}"
                }
            response = Response(json.dumps(invalidUsernameErrorMsg), status=400, mimetype='application/json')
            return response

        email = data['email']     
        if not re.match(r"^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$", email):
            invalidEmailErrorMsg = {
                "error": "Invalid email passed in request",
                "helpString": "Email must have @ characters, data to be passed similar to this {'email': 'Jessica@storeapp.co.ke'}"
                }
            response = Response(json.dumps(invalidEmailErrorMsg), status=400, mimetype='application/json')
            return response

        password = data['password']    
        if not re.match("^[a-zA-Z0-9_]*$", password):
            invalidpasswordErrorMsg = {
                "error": "Password cannot be blank or have special characters",
                "helpString": "Enter start password , data to be passed similar this {'password': 'test123'}"
                }
            response = Response(json.dumps(invalidpasswordErrorMsg), status=400, mimetype='application/json')
            return response
      
        user = UserModel(
            data['username'],
            data['email'],
            data['password']
            )
        ListDatabase.USERS.append(user)
        response = user.resultant()
        return {'status': 'Registration Successful', "user": response}, 201


class Login(Resource):
    def post(self):
       
        data = request.get_json()
        username = data['username'] or data['email']
        password = data['password']

#  validate user input
        if not username:
            return {'message': 'username cannot be empty'},400

        if not password:
            return {'message': 'password cannot be empty'},400

# checks if a user with the username exists
        user = ListDatabase.get_user_by_username(username)
        if not user:
            return {'message': 'not found'}
       
      
# compare user password with stored password in USERS list
        user = ListDatabase.get_user_by_password(password)
        print(user)
        if not user:
            return {'message': 'not found'}

        return {'msg': 'user login succesful', 'user': username}, 200

        
class Allusers(Resource):
    def get(self):
        user = [user.resultant() for user in ListDatabase.USERS]
        return{'msg': 'Retrival of all users successul', "users":user}, 200