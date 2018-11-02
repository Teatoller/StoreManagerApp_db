from flask import Flask, jsonify, request
from db import db_connection
import psycopg2.extras
cursor = db_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)


class SaleModel():

    def __init__(self, name=None, price=None, quantity=None,
                 category=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        
    def savesale(self):
        sale = "INSERT INTO sales(name, price, quantity, category)\
                   VALUES('%s','%s', '%s', '%s')" % (
                    self.name, self.price, self.quantity, self.category)
        return cursor.execute(sale)

    def get_by_sale_id(self, id):
        query = "SELECT * FROM sales WHERE sale_id={};".format(id)
        cursor.execute(query)
        p = cursor.fetchone()
        return p
        
    def get_all(self):
        query = "SELECT * FROM sales"
        cursor.execute(query)
        return cursor.fetchall()

    def delete_by_id(self, id):
        query = "DELETE FROM sales WHERE sale_id={};".format(id)
        return cursor.execute(query)