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

    def get_by_product_id(self, id):
        query = "SELECT * FROM products WHERE product_id={};".format(id)
        cursor.execute(query)
        p = cursor.fetchone()
        return p
        
    def get_all(self):
        query = "SELECT * FROM products"
        cursor.execute(query)
        return cursor.fetchall()

    def delete_by_id(self, id):
        query = "DELETE FROM products WHERE product_id={};".format(id)
        return cursor.execute(query)


