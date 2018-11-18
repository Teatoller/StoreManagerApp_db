from flask_restful import Resource
from flask import Flask, jsonify, request, Response, make_response
from app.api.v2.models.products import ProductModel
from db import db_connection
import json
from flask_jwt_extended import jwt_required, get_jwt_identity


class Product(Resource):
    @jwt_required
    def post(self):
        # user_detail = UserModel().get_by_username(get_jwt_identity())
        # if user_detail['role'] == "user":
        #     return{'msg': 'not authorised access denied'}, 401

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

    @jwt_required
    def get(self, id=None):
        """ Gets Single product """
        if not id:
            product = ProductModel()
            products = product.get_all()
            all_products = []
            for p in products:
                format_pAll = {
                    'id': p[0],
                    'name': p[1],
                    'price': p[2],
                    'quantity': p[3],
                    'category': p[4]
                    }
                all_products.append(format_pAll)
            return {"status": "successful",
                    "products": all_products}, 200

        product = ProductModel.get_by_product_id(self, id)

        if product:
            format_p = {
                "id": product[0],
                "name": product[1],
                "price": product[2],
                'quantity': product[3],
                'category': product[4]
            }
            return {"status": "successful",
                    "product": format_p}, 200
        return {"status": "unsuccesful!", "msg": "product not in stock"}, 404

    @jwt_required
    def put(self, id=None):
        if not id:
            return make_response(jsonify({"msg": "inventory is needed"}), 422)
        data = request.get_json()
        user = get_jwt_identity

        if data is not None and not Product.get_by_product_id(self, id):
            return make_response(jsonify({"msg": "product not available"}), 404)

    @jwt_required
    def delete(self, id=None):
        """ Deletes a Single product """
        product = ProductModel()
        if not id:
            return make_response(jsonify({'msg': 'no related prod id'}, 422))
        else:
            if ProductModel.get_by_product_id(self, id) is not None:
                ProductModel.delete_by_id(self, id)
                return make_response(jsonify(
                 {'message': 'product deleted succesfully'}), 200)
            else:
                return make_response(jsonify(
                {'message': 'product not found'}), 404)
