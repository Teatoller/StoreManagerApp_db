import unittest
from flask import json
from app import create_app
from app.api.v1.models.sales import ListDatabase

config_name = "testing"
app = create_app(config_name)

p_url = 'api/v1/sales'


class TestSale(unittest.TestCase):
    """ Sale Testing Module """

    def setUp(self):
        """ Method to call up the tests"""
        app.testing = True
        self.app = app.test_client()

        self.sale_data = {
            "name": "Cabin",
            "price": 50000,
            "quantity": 1,
            "category": "Deluxe"
        }

    def test_add_sale(self):
        """ Checks if sale can actually be posted """
        response = self.app.post(p_url,
                                 data=json.dumps(self.sale_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_sales(self):
        """ Test get method for all sale """
        self.app.post(p_url,
                      data="Sales_data",
                      content_type='application/json')
        response = self.app.get(p_url)
        self.assertEqual(response.status_code, 200)

    def test_get_single_sale(self):
        """ Test Method to a for single sale  """
        self.app.post(p_url,
                      data=self.sale_data,
                      content_type='application/json')
        sale = ListDatabase.get_sale_by_name('Cabin')
        sale_id = sale.sale_id
        sale = self.app.get('/api/v1/sales/{}'.format(sale_id))
        self.assertEqual(sale.status_code, 200)
        