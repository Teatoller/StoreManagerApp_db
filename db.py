import psycopg2
from psycopg2 import Error
import os
from Instance.config import app_config

config_name = os.getenv('APP_SETTINGS')
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_TEST_URL = os.getenv('DATABASE_TEST_URL')
release_url = os.getenv('release_url')


def db_connection():
        try:
                if config_name == 'development':
                        connection = psycopg2.connect(DATABASE_URL)
                elif config_name == 'testing':
                        connection = psycopg2.connect(DATABASE_TEST_URL)
                else:
                        connection = psycopg2.connect(release_url)
                connection.autocommit = True
                return connection
        except (Exception, psycopg2.DatabaseError) as error:
                return "Error while connecting to PostgreSQL", error


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
