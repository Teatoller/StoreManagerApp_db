import psycopg2
from psycopg2 import Error
import pprint
import os

class Data():
    def __init__(self):
        try:
            url =  "host='localhost' dbname='dbStoreman' user='postgres1' password='secret'"
            self.con = psycopg2.connect(url)
            self.con.autocommit = True
            self.cursor = self.con.cursor()
        except(Exception, psycopg2.DatabaseError) as error:
            pprint("Cannot connect to database" , error)


    def create_table(self):
        self.cursor.execute("CREATE TABLE storerecord (id serial PRIMARY KEY, name varchar(30), age integer NOT NULL)")



if __name__ == '__main__':
    database_conn = Data()
    database_conn.create_table()