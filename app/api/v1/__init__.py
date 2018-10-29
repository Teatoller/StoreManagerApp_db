from flask import Blueprint
from flask_restful import Api

# Defines the blueprint application
# Local imports
from app.api.v1.views.products import Product, Products
from app.api.v1.views.sales import Sale, Sales
from app.api.v1.views.users import Registration, Login, Allusers, User

version_1 = Blueprint('api', __name__, url_prefix="/api/v1")
api = Api(version_1)

#  Adding a resource to api class for products
api.add_resource(Products, '/products/')
api.add_resource(Product, '/products/<int:id>')

#  Adding a resource to api class for sales
api.add_resource(Sales, '/sales')
api.add_resource(Sale, '/sales/<int:id>')

# # Adding a resource to api for Registration and login
api.add_resource(Registration, '/registrations')
api.add_resource(Login, '/logins')

api.add_resource(Allusers, '/users')
api.add_resource(User, '/users/<int:id>')