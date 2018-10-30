class UserModel():
    """ """

    user_id = 1

    def __init__(self, firstname, lastname, username, email, password, role):
        """ """
        self.user_id = UserModel.user_id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        UserModel.user_id += 1

    def resultant(self):
        """ """
        return dict(
            username=self.username,
            email=self.email,
            password=self.password
        )
    # @staticmethod
    # def get_user_by_username(username):
    #     """ """
    #     for user in USERS:
    #         if user['username'] == username:
    #             return user
    #         return 0


class RevokedTokenModel():
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

    # @jwt_required
    # @classmethod
    # def get_user_id(cls, user_id):
    #     for user in cls.USERS:
    #         if user.user_id == user_id:
    #             return user
    # @jwt_required
    # @classmethod
    # def get_user_by_username(cls, username):
    #     """ """
    #     for user in cls.USERS:
    #         if user.username == username:
    #             return user
    #         return 0
    # @jwt_required
    # @classmethod
    # def get_user_by_password(cls, password):
    #     """ """
    #     for user in cls.USERS:
    #         if user.password == password:
    #             return user
    #         return 0