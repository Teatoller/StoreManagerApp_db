from flask_restful import Resource
from flask import Flask, jsonify, request, Response, make_response
from app.api.v2.models.sales import SaleModel
from db import db_connection
import json
from flask_jwt_extended import jwt_required, get_jwt_identity


class Sale(Resource):
    @jwt_required
    def post(self):
        user_detail = UserModel().get_by_username(get_jwt_identity())
        if user_detail['role'] == "admin":
            return{'msg': 'Access denied, only for Store attendants'}, 401

        """ Add and validates sale that is added """
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

    @jwt_required
    def get(self, id=None):
        """ Gets Single sale """
        if not id:
            sale = SaleModel()
            sales = sale.get_all()
            all_sales = []
            for s in sales:
                format_sAll = {
                    'id': s[0],
                    'name': s[1],
                    'price': s[2],
                    'quantity': s[3],
                    'category': s[4]
                    }
                all_sales.append(format_sAll)
            return {"status": "successful",
                    "sales": all_sales}, 200

        sale = SaleModel.get_by_sales_id(self, id)

        if sale:
            format_s = {
                "id": sale[0],
                "name": sale[1],
                "price": sale[2],
                'quantity': sale[3],
                'category': sale[4]
            }
            return {"status": "successful",
                    "sale": format_s}, 200
        return {"status": "unsuccesful!", "msg": "sale not in record"}, 404

    @jwt_required
    def put(self, id=None):
        if not id:
            return make_response(jsonify({"msg": "sale is needed"}), 422)
        data = request.get_json()
        user = get_jwt_identity

        if data is not None and not Sale.get_by_sales_id(self, id):
            return make_response(jsonify({"msg": "sale not possible"}), 404)

    @jwt_required
    def delete(self, id):
        sale = SaleModel()
        sale.delete_by_sales_id(id)
        return make_response(jsonify(
                {'msg': 'sale deleted succesfully'}), 200)
