from flask import Flask, jsonify, request
from flask_jwt_extended import(JWTManager, jwt_optional,
                               create_access_token,
                               get_jwt_identity, get_raw_jwt, jwt_required)


class UserModel():
    """ """

    def __init__(self, firstname, lastname, username, email, password, role):
        """ """
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.role = role
    
    def saveuser(self):
        """ """
        user = ("INSERT INTO users(firstname, lastname, username, email, password, role) VALUES(%s, %s, %s, %s, %s, %s);",
                       (firstname, lastname, username, email, password, role))
        cursor = db_connection().cursor()
        cursor.execute(user)
        db_connection().commit()

    def Resultant(self):
        """ """
        return dict(
            firstname=self.firstname,
            lastname=self.lastname,            
            username=self.username,
            email=self.email,
            password=self.password,
            role=self.role
        )


class RevokedTokenModel():
    """ """
    blackedlist = ()

    def check_if_token_blacklisted():
        jti = decrypted_token['jti']
        return jti in blackedlist


class Refreshtokenrequired():
    """Docstring revokes current user access token """
    def refresh():
        current_user = get_jwt_identity()
        ret_tkn = {'access_token': create_access_token(identity=current_user)}
        return jsonify(ret_tkn), 200


class jwt_required():
    """Docstring prevents blacklisted tokens from re-use """
    def protected():
        return jsonify({'msg': 'Restricted access'})

    @classmethod
    @jwt_required
    def get_user_id(cls, user_id):
        for user in cls.users:
            if user.user_id == user_id:
                return user
    
    @classmethod
    @jwt_required
    def get_user_by_username(cls, username):
        """ """
        for user in cls.users:
            if user.username == username:
                return user
            return 0

    @classmethod
    @jwt_required
    def get_user_by_password(cls, password):
        """ """
        for user in cls.userstable:
            if user.password == password:
                return user
            return 0