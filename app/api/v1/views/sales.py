from flask_restful import Resource
from flask import request
from app.api.v1.models.sales import SaleModel, ListDatabase


class Sale(Resource):
    def get(self, id):
        """ Method to return a single sale from SALES list """
        sale = ListDatabase.get_sale_id(id)
        if sale:
            return {"status": "successful", "sale": sale.resultant()}, 200
        return {"status": "unsuccesful!", "msg": "sale not found"}, 404


class Sales(Resource):
    def post(self):
        """ Method for validating and adding Sale """
        data = request.get_json(force=True)
        if 'name' not in data:
            return {"msg": "please input name"}, 406
        if 'price' not in data:
            return {"msg": "please input price :"}, 406
        if 'quantity' not in data:
            return{"msg": "Stock is Nil"}, 406
        if 'category' not in data:
            return{"msg": "Stock is not categorized"}, 406


        sale = SaleModel(
            data['name'],
            data['price'],
            data['quantity'],
            data['category'])
        ListDatabase.SALES.append(sale)
        response = sale.resultant()
        return {"status": "The sale was made successfully!", "sale": response}, 201

    def get(self):
        """ Iterates and loop SALES list and returns all items in
         SALES  database"""
        sale = [sal.resultant() for sal in ListDatabase.SALES]
        return {"status": "Retrieval of sale records successful!", "sales": sale}, 200