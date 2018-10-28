import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="user_1",
                                  password="test123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="storemanager_db")
    cursor = connection.cursor()

    salestable = ''' CREATE TABLE IF NOT EXISTS sales
            (sales_id int, name varchar(255),
            price varchar(255),
            quantity varchar(255),
            category varchar(255)); '''

    cursor.execute(salestable)
    connection.commit()

    salestable = ''' CREATE TABLE IF NOT EXISTS sales
            (sales_id int,
            name varchar(255),
            price varchar(255),
            quantity varchar(255),
            category varchar(255)); '''

    cursor.execute(salestable)
    connection.commit()

    productstable = ''' CREATE TABLE IF NOT EXISTS sales
            (product_id int,
            name varchar(255),
            price varchar(255),
            quantity varchar(255),
            category varchar(255)); '''
    cursor.execute(productstable)
    connection.commit()

    userstable = ''' CREATE TABLE IF NOT EXISTS sales
            (user_id int,
            first_name character varying(50) NOT NULL,
            last_name character varying(50),
            username character varying(50) NOT NULL,
            email character varying(50)); '''
    cursor.execute(userstable)
    connection.commit()

    print("Table created successfully in PostgreSQL ")
    
except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
