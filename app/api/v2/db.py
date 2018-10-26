import os
import psycopg2

db_url = "dbname=steve user=postgres password=Jayne123"

try:
    con = psycopg2.connect(db_url)
except:
    print("The database connection has failed")

cur = con.cursor()


def salestable():
    usertable = (
        """
        CREATE TABLE sales(
            product_id int,
            name varchar(255),
            price varchar(255),
            quantity varchar(255),
            category varchar(255));"""
            )
    cur.execute(userstable)
    cur.commit()

# def userstable():
#     userstable = (
#         """
#         CREATE TABLE users(
#             user_id int,
#             Username varchar(255),
#             Email varchar(255),
#             Password varchar(255));"""
#             )
#     cur.execute(userstable)
#     cur.commit()

# def productstable():
#     usertable = (
#         """
#         CREATE TABLE products(
#             product_id int,
#             name varchar(255),
#             price varchar(255),
#             quantity varchar(255),
#             category varchar(255));"""
#             )
#     cur.commit




