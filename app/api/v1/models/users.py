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
            user_name=self.username,
            user_email=self.email,
            user_password=self.password
        )


class ListDatabase():
    PRODUCTS = []
    SALES = []
    USERS = []

    @classmethod
    def get_user_by_id(cls, user_id):
        for user in cls.USERS:
            if user.user_id == user_id:
                return user

    @classmethod
    def get_user_by_username(cls, username):
        """ """
        for user in cls.USERS:
            if user.username == username:
                return user
