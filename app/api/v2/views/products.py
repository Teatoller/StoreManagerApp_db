from flask_restful import Resource
from flask import Flask, jsonify, request, Response, make_response
from app.api.v2.models.products import ProductModel
from db import db_connection
import json


class Products(Resource):
    def post(self):
        """ Add and validates product that are added """
        data = request.get_json()
        if 'name' not in data:
            return {"msg": "please input name"}, 406
        if 'price' not in data:
            return {"msg": "please input price"}, 406
        if 'quantity' not in data:
            return {"msg": "please input quantity"}, 406
        if 'category' not in data:
            return {"msg": "please input category"}, 406

        product = ProductModel(
            data['name'],
            data['price'],
            data['quantity'],
            data['category'])
        product.saveproduct()
        return make_response(jsonify(
                {'msg': 'product created succesfully'}), 201)
