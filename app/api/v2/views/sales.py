from flask_restful import Resource
from flask import Flask, jsonify, request, Response, make_response
from app.api.v2.models.sales import SaleModel
from db import db_connection
import json
from flask_jwt_extended import jwt_required, get_jwt_identity


class Sale(Resource):
    def post(self):
        """ Add and validates sales that are added """
        data = request.get_json()
        if 'name' not in data:
            return {"msg": "please input name"}, 406
        if 'price' not in data:
            return {"msg": "please input price"}, 406
        if 'quantity' not in data:
            return {"msg": "please input quantity"}, 406
        if 'category' not in data:
            return {"msg": "please input category"}, 406

        sale = SaleModel(
            data['name'],
            data['price'],
            data['quantity'],
            data['category'])
        sale.savesale()
        return make_response(jsonify(
                {'msg': 'sale created succesfully'}), 201)

    def get(self, id=None):
        """ Gets Single sale """
        if not id:
            sale = SaleModel()
            sales = sale.get_all()
            return {"status": "successful",
                    "sale": sales}, 200

        sale = SaleModel.get_by_sale_id(self, id)
        
        if sale:
            format_p = {
                "id": product[0],
                "name": product[1],
                "price": product[2],
                'quantity': product[3],
                'category': product[4]
            }
            return {"status": "successful",
                    "sale": format_p}, 200
        return {"status": "unsuccesful!", "msg": "sale not is viable"}

    def put(self, id=None):
        if not id:
            return make_response(jsonify({"msg": "sale is needed"}), 422)
        data = request.get_json()
        user = get_jwt_identity

        if data != None and not Sale.get_by_sale_id(self, id):
            return make_response(jsonify({"msg": "sale not made"}), 404)

    def delete(self, id):
        sale = SaleModel()
        sale.delete_by_id(id)
        return make_response(jsonify(
                {'msg': 'sale deleted succesfully'}), 201)
          