from flask import Blueprint
from flask_restful import Api

# Defines the blueprint application

from app.api.v2.views.users import (Signup, Login)
from app.api.v2.views.products import (Products, Product)

version_2 = Blueprint('api', __name__, url_prefix="/api/v2")
api = Api(version_2)

api.add_resource(Signup, '/auth/signup')
api.add_resource(Login, '/auth/login')
api.add_resource(Products, '/products')
api.add_resource(Product, '/products/<int:id>')
