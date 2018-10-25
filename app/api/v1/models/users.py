from flask_restful import Resource
from flask import request
from app.api.v1.models.users import UserModel, ListDatabase
import re
from werkzeug.security import generate_password_hash, \
     check_password_hash

 

class Registration(Resource):
    def post(self):
        data = request.get_json(force=True)
        valid_username = "".join(data['username'].split())

        if  len(valid_username)<6:
            return {"msg":" username is less than six characters"}, 406
        username = data['username']
        
        if not re.match("^[a-zA-Z0-9_]*$", username):
            return {"msg":" username not valid"}, 406
    
        email = data['email']     
        if not re.match(r"^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$", email):
            return {"msg":" Email not valid"}, 406

                
        user = UserModel(
            data['username'],
            data['email'],
            data['password']
            )        

        ListDatabase.USERS.append(user)
        response = user.resultant()
        return {'status':'Registration Successful', "user": response}, 201

class Login(Resource):
    def post(self):
       
        data =  request.get_json()
        username = data['username'] or data['email']
        password = data['password']

#  validate user input
        if not username:
            return {'message':'username cannot be empty'},400

        if not password:
            return {'message':'password cannot be empty'},400

# checks if a user with the username exists
        user = ListDatabase.get_user_by_username(username)
        if not user:
            return {'message':'not foundfcgvhbj'}
        
            

# compare user password with stored password in USERS list
        user = ListDatabase.get_user_by_password(password)
        print(user)
        if not user:
            return {'message':'not foundp'}


        return {'msg':'user login succesful', 'user':username }, 200

        
class Allusers(Resource):
    def get(self):
        user = [user.resultant() for user in ListDatabase.USERS]
        return{'msg': 'Retrival of all users successul', "users":user}, 200