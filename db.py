import psycopg2
from psycopg2 import Error
import os
from Instance.config import app_config

config_name = os.getenv('APP_SETTINGS')
db_url = os.getenv('DATABASE_URL')
db_test_url = os.getenv('DATABASE_TEST_URL')
release_url = os.getenv('release_url')


def db_connection():
        try:
                if config_name == 'development':
                        connection = psycopg2.connect(db_url)
                elif config_name == 'testing':
                        connection = psycopg2.connect(db_test_url)
                else:
                        connection = psycopg2.connect(release_url)
                connection.autocommit = True
                return connection
        except (Exception, psycopg2.DatabaseError) as error:
                print('Databse error encountered trying to reconnect again...')
                connection = psycopg2.connect(db_test_url)
                return connection




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


def create_default_admin():
        cursor = db_connection().cursor()
        firstname = 'Storemanager',
        lastname = 'Owner',
        username = 'defaultadmin'
        password = 'test123'
        role = 'admin'

        query = "SELECT * FROM users WHERE username=%s"
        cursor.execute(query, (username,))
        data = cursor.fetchone()

        if not data:
                query = "INSERT INTO users(firstname, lastname, username, email," \
                 " password,role) VALUES('%s','%s', '%s', '%s', '%s', '%s')" % (
                    self.firstname, self.lastname, self.username, self.email,
                    self.password, self.role)                
        return cursor.execute(query)
