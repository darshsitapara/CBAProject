import mysql.connector
from mysql.connector import Error


def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='storedata',
            user='root',
            password='d0903PF!'
        )
    except Error as e:
        print(f"error: '{e}' occurred")
    return connection


def execute_read_query(query, parameters=None):
    cursor = None
    connection = get_db_connection()
    result = None
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, parameters or ())
        result = cursor.fetchall()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return result


def execute_write_query(query, parameters):
    cursor = None
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        connection.commit()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
