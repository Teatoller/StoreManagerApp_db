from flask_restful import Resource
from flask import request
from app.api.v1.models.users import UserModel, ListDatabase


class Registration(Resource):
    def post(self):
        data = request.get_json(force=True)

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
        data = request.get_json(force=True)

        user = UserModel(
            data['username'],
            data['email'],
            data['password']
        )
        ListDatabase.USERS.append(user)
        response = user.resultant()
        return {'msg': 'user login succesful', "current_user": response}, 201


class Allusers(Resource):
    def get(self):
        user = [user.resultant() for user in ListDatabase.USERS]
        return{'msg': 'Retrival of all users successul', "users": user}, 200