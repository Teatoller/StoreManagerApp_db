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

    invalidsignup_data = {
        "firstname": "Steven1",
        "lastname": "Ennis",
        "username": "Teat#oller",
        "email": "steven@gmail.co.ke",
        "password":"test123",
        "role": "admin"
        }

    invalidemail_data = {
        "firstname": "Steven1",
        "lastname": "Ennis",
        "username": "Teatoller",
        "email": "stevengmail.co.ke",
        "password":"test123",
        "role": "admin"
        }

    invalidlenusername_data = {
        "firstname": "Steven1",
        "lastname": "Ennis",
        "username": "Teatr",
        "email": "stevengmail.co.ke",
        "password":"test123",
        "role": "admin"
        }

    invalidpassword_data = {
        "firstname": "Steven1",
        "lastname": "Ennis",
        "username": "Teatoller",
        "email": "steven@gmail.co.ke",
        "password": "test12#3",
        "role": "admin"
        }

    invalid_no_username_data = {
        "firstname": "Steven1",
        "lastname": "Ennis",
        "username": " ",
        "email": "steven@gmail.co.ke",
        "password": "test12#3",
        "role": "admin"
        }

    invalid_no_password_data = {
        "firstname": "Steven1",
        "lastname": "Ennis",
        "username": "Teatoller",
        "email": "steven@gmail.co.ke",
        "password": " ",
        "role": "admin"
        }

    def setUp(self):
        """ Method to call up the tests"""
        app.testing = True
        self.app = app.test_client()
     
    def test_signup(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(self.signup_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_invalidsignup_data(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(self.invalidsignup_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalidemail_data(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(self.invalidemail_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalidlenusername_data(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(self.invalidlenusername_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalidpassword_data(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(self.invalidpassword_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_no_username_data(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(self.invalidpassword_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_no_password_data(self):
        """ """
        response = self.app.post(p1_url,
                                 data=json.dumps(self.invalid_no_password_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400) 

    def test_Login(self):
        """ """
        response = self.app.post(p2_url,
                                 data=json.dumps(self.login_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

