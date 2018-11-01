import unittest
from flask import json
from app import create_app

config_name = "testing"
app = create_app(config_name)

p1_url = 'api/v2/auth/signup'
p2_url = 'api/v2/auth/login'


class TestUsers(unittest.TestCase):
    """ Users Testing Module """

    signup_data = {
        "firstname": "Steven1",
        "lastname": "Ennis",
        "username": "Teatoller",
        "email": "steven@gmail.co.ke",
        "password":"test123",
        "role": "admin"
        }

    login_data = {
        "username": "Teatoller",
        "password": "test123"        
        }

    def setUp(self):
        """ Method to call up the tests"""
        app.testing = True
        self.app = app.test_client()
     
    def test_Signup(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(self.signup_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_Login(self):
        """ """
        response = self.app.post(p2_url,
                                 data=json.dumps(self.login_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)

