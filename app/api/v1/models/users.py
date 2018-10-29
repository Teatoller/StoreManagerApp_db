class UserModel():
    """ """

    user_id = 1

    def __init__(self, username, email, password):
        """ """
        self.user_id = UserModel.user_id
        self.username = username
        self.email = email
        self.password = password
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


class ListDatabase():
    
    USERS = []

    @classmethod
    def get_user_id(cls, user_id):
        for user in cls.USERS:
            if user.user_id == user_id:
                return user

    @classmethod
    def get_user_by_username(cls, username):
        """ """
        for user in cls.USERS:
            if user.username == username:
                return user
            return 0

    @classmethod
    def get_user_by_password(cls, password):
        """ """
        for user in cls.USERS:
            if user.password == password:
                return user
            return 0