from flask import Flask, jsonify, request
from db import db_connection
import psycopg2.extras
cursor = db_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)


class ProductModel():

    def __init__(self, name=None, price=None, quantity=None,
                 category=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        
    def saveproduct(self):
        product = "INSERT INTO products(name, price, quantity, category)\
                   VALUES('%s','%s', '%s', '%s')" % (
                    self.name, self.price, self.quantity, self.category)
        return cursor.execute(product)

    def get_by_product(self, name, category):
            query = "SELECT * from products WHERE product='%s' AND category='%s';" % (product, category)
            cursor.execute(query)
            product = cursor.fetchone()
            return product
