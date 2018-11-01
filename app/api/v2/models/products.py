from flask import Flask, jsonify, request
from db import db_connection
import psycopg2.extras
cursor = db_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)


class UserProduct():

    def __init__(self, name=None, price=None, quantity=None,
                 category=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        
    def saveproduct(self):
        product = "INSERT INTO users(name, price, quantity, category)\
                   VALUES('%s','%s', '%s', '%s')" % (
                    self.name, self.price, self.quantity, self.category)
        return cursor.execute(product)
        