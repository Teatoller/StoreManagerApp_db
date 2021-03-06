from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash
from db import db_connection
import psycopg2.extras
cursor = db_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)


class UserModel():

    def __init__(self, firstname=None, lastname=None, username=None,
                 email=None, password=None, role=None):
        hashed = ""
        if password:
            hashed = generate_password_hash(password)
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = hashed
        self.role = role

    def saveuser(self):
        user = "INSERT INTO users(firstname, lastname, username, email," \
               " password,role) VALUES('%s','%s', '%s', '%s', '%s', '%s')" % (
                    self.firstname, self.lastname, self.username, self.email,
                    self.password, self.role)
        return cursor.execute(user)

    def get_by_username(self, username):
        query = "SELECT * FROM users WHERE username=%s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        return user


def get_by_email(email):
    query = "SELECT * FROM users WHERE email='%s';" % (email,)
    cursor.execute(query)
    user = cursor.fetchone()
    return user
