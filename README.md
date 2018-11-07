# StoreManagerApp_db
Store Manager is a web application that helps store owners manage sales and product inventory records.
[![Build Status](https://travis-ci.org/Teatoller/StoreManagerApp_db.svg?branch=master)](https://travis-ci.org/Teatoller/StoreManagerApp_db) [![Coverage Status](https://coveralls.io/repos/github/Teatoller/StoreManagerApp_db/badge.svg?branch=ft-Add-Sale-endpoints-161650429)](https://coveralls.io/github/Teatoller/StoreManagerApp_db?branch=ft-Add-Sale-endpoints-161650429) [![Maintainability](https://api.codeclimate.com/v1/badges/6ab555b0a04d536d0a1e/maintainability)](https://codeclimate.com/github/Teatoller/StoreManagerApp_db/maintainability)

#### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

Installation
The development version can be downloaded from its page at GitHub.

#### Create a project folder and a env folder within:

$ mkdir myproject
$ cd myproject
$ python3 -m venv env

$ git clone https://github.com/Teatoller/StoreManagerApp_db.git 
$ cd StoreManager_db

GET /sales

Get all sale records.
$ export FLASK_APP=run.py
$ flask run

* Running on http://127.0.0.1:5000/

### Prerequisites
What things you need to install

$ pip Install Flask
$ pip install flask-restful
$ pip instal flask-jwt-extended

A step by step series of examples that tell you how to get a development env running

1. Open postman
2. Copy the link 'http://127.0.0.1:5000/' and paste in the terminal .
3. Add endpoint after the .5000/*****

Example 

a. In Postman in the field adjacent tp "PARAM" ENTER 'http://127.0.0.1:5000/api/v2/products'

b. In body area on server side use this is the format;

{
    "name": "Nescafe"
    "price": 15
    "quantity": 1
    "category": "Beverage"
}

i. You will get a message that you are not authorized because you are either not registered or you do not have a token.

ii. Sign yourself up.
{
    "firstname": "Jessica",
    "lastname"; "Drews",
    "username": "Jessy12",
    "email": "Jessy@storemanagerap.co.ke,
    "password": "test123",
    "role": "user"
}
iii. Login
{
    "username": "Jessy12",
    "password": "test123"
}
iv. Use the token generated to by;
a. clicking on header, check the Authorization box, inline just under value type Bearer <'token'>

c. The products will display on the browser side of Postman and get posted in the database.

d .Try with a different product items.
e. Now, change the;

i. POST TO GET 
ii. Change route to 'http://127.0.0.1:5000/api/v2/products' and then send. 

iii. You should see returned all the products you posted.

NB. Ensure the content-header JSON(application/json)

This are the endpoint routes you may want to try:

Prefix '/api/v2'

#### Signup and login endpoints
'/auth/signup'
'/auth/login'

#### endpoint="get all and post product
'/products'

#### endpoint="specific product
'/products/<int:id>'
####  endpoint="get all and post sale
'/sales'
#### endpoint="specific sale"
'/sales/<int:id>'

#### Fetch a single product record
Get a specific product using the product’s id.
GET /<'products/<int:Id>

Versioning
This is v2 built with Flask restful

Authors
Steven Ennis as part of fulfilment in Andela Pre-Bootcamp.
