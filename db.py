import psycopg2
from psycopg2 import Error
import os

user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DATABASE')


def db_connection():
        try:
                connection = psycopg2.connect(user=user,
                                              password=password,
                                              host=host,
                                              port=port,
                                              database=database)
                connection.autocommit = True
                return connection
        except (Exception, psycopg2.DatabaseError) as error:
                print("Error while connecting to PostgreSQL", error)


def create_tables():
        cursor = db_connection().cursor()
      
        sales_table = """ 
                        CREATE TABLE IF NOT EXISTS sales
                        (sales_id serial PRIMARY KEY,
                        name varchar(255),
                        price varchar(255),
                        quantity varchar(255),
                        category varchar(255));"""
   
        product_stable = """
                        CREATE TABLE IF NOT EXISTS products
                        (product_id serial PRIMARY KEY,
                        name varchar(255),
                        price varchar(255),
                        quantity varchar(255),
                        category varchar(255));"""

        users_table = """
                        CREATE TABLE IF NOT EXISTS users
                        (user_id serial PRIMARY KEY,
                        firstname character varying(250) NOT NULL,
                        lastname character varying(250),
                        username character varying(250) NOT NULL,
                        email character varying(250),
                        password character varying(250) NOT NULL,
                        role character varying(250));"""

        tables = [users_table, product_stable, sales_table]
               
        for table in tables:
                cursor.execute(table)

