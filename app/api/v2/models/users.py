from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash
from db import db_connection


class UserModel():

    def __init__(self, firstname, lastname, username, email, password, role):
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
        cursor = db_connection().cursor()
        return cursor.execute(user)

    def get_by_username(self, username):
        user = "SELECT * from users WHERE username=%s (username)"
        cursor = db_connection().cursor()
        return cursor.execute(user)
