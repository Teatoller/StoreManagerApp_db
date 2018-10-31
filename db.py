import psycopg2
from psycopg2 import Error


def db_connection():
        try:
                connection = psycopg2.connect(user="user_1",
                                              password="test123",
                                              host="127.0.0.1",
                                              port="5432",
                                              database="storemanager_db")
                connection.autocommit = True
                return connection
        except (Exception, psycopg2.DatabaseError) as error:
                print("Error while connecting to PostgreSQL", error)


def create_tables():
        cursor = db_connection().cursor()
      
        sale_stable = """ 
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

        user_stable = """
                        CREATE TABLE IF NOT EXISTS users
                        (user_id serial PRIMARY KEY,
                        firstname character varying(50) NOT NULL,
                        lastname character varying(50),
                        username character varying(50) NOT NULL,
                        email character varying(50),
                        password character varying(50) NOT NULL,
                        role character varying(50));"""

        tables = [users_table, product_stable, sales_table]
               
        for table in tables:
                cursor.execute(table)

