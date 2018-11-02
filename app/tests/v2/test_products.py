import unittest
from flask import json
from app import create_app

config_name = "testing"
app = create_app(config_name)

p1_url = 'api/v2/products'
p2_url = 'api/v2/products/<int:id>'


class TestProducts(unittest.TestCase):
    """ Users Testing Module """

    product_data = {
        "name": "Elianto",
        "price": 167,
        "quantity": 2,
        "category": "Salad"        
        }

    invalid_no_name_product_data = {
        "name": "",
        "price": 167,
        "quantity": 2,
        "category": "Salad"        
        }

    invalid_no_price_product_data = {
        "name": "",
        "price": 167,
        "quantity": 2,
        "category": "Salad"        
        }

    invalid_no_quantity_product_data = {
        "name": "",
        "price": 167,
        "quantity": 2,
        "category": "Salad"        
        }

    invalid_no_category_product_data = {
        "name": "",
        "price": 167,
        "quantity": 2,
        "category": "Salad"        
        }
    
    def setUp(self):
        """ Method to call up the tests"""
        app.testing = True
        self.app = app.test_client()
     
    def test_product_data(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(self.product_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)
    
    def test_invalid_noname_product_data(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(
                                     self.invalid_no_name_product_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_invalid_no_price_product_data(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(
                                     self.invalid_no_price_product_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_invalid_no_quantity_product_data(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(
                                     self.invalid_no_quantity_product_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_invalid_no_category_product_data(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(
                                     self.invalid_no_category_product_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)
