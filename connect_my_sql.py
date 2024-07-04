import mysql.connector
from mysql.connector import Error # Tells us if there are any errors to our connection

def connect_db():
    db_name = "library_management_db" # The actual database name not connection name
    user = "root"
    password = "Sennenga28!"
    host = "localhost"

#attempt to connect
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        # check if the connection is successful
        if conn.is_connected():
            print("Connected to MySQL Database successfully")
            return conn
    except Error as e:
        print(f"Error: {e}")
    
    # finally:
    #     if conn and conn.is_connected():
    #         conn.close()
    #         print("MySql Connection is closed.")

connect_db()