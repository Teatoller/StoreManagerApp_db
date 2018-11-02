from flask import Blueprint
from flask_restful import Api

# Defines the blueprint application

from app.api.v2.views.users import (Signup, Login)
from app.api.v2.views.products import Product
from app.api.v2.views.sales import Sale

version_2 = Blueprint('api', __name__, url_prefix="/api/v2")
api = Api(version_2)

api.add_resource(Signup, '/auth/signup')
api.add_resource(Login, '/auth/login')
api.add_resource(Product, '/products', endpoint="get all and post product")
api.add_resource(Product, '/products/<int:id>', endpoint="specific product")
api.add_resource(Sale, '/sales', endpoint="get all and post sale")
api.add_resource(Sale, '/sales/<int:id>', endpoint="specific sale")

