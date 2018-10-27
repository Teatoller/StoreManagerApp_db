import unittest
from flask import json
from app import create_app
from app.api.v1.models.product import ListDatabase

config_name = "testing"
app = create_app(config_name)

# Assigns the endpoint path to the variable p_url
p_url = 'api/v1/products'


class TestProduct(unittest.TestCase):
    """ Product Testing Module """

    def setUp(self):
        """Method to call up the tests """
        app.testing = True
        self.app = app.test_client()

        self.product_data = {
            "name": "Cabin",
            "price": 500000,
            "quantity": 1,
            "category": "Deluxe"
        }

    def test_add_product(self):
        """ Checks if products can actually be posted """
        response = self.app.post(p_url,
                                 data=json.dumps(self.product_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_products(self):
        """ Test get method for all products """
        self.app.post(p_url,
                      data=self.product_data,
                      content_type='application/json')
        response = self.app.get(p_url)
        self.assertEqual(response.status_code, 200)

    def test_get_single_product(self):
        """ Tst get single product by product Id """
        self.app.post(p_url,
                      data=self.product_data,
                      content_type='application/json')
        product = ListDatabase.get_product_by_name('Cabin')
        prod_id = product.product_id
        product = self.app.get('/api/v1/products/{}'.format(prod_id))
        self.assertEqual(product.status_code, 200)
        