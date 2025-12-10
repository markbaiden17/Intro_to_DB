import mysql.connector

CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'AkorfAntAkosM@ns44'
}

DATABASE_NAME = 'alx_book_store'

def create_database():
    mydb = None
    mycursor = None

    try:
        mydb = mysql.connector.connect(**CONFIG)
        mycursor = mydb.cursor()

        sql_command = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
        mycursor.execute(sql_command)

        print(f"Database '{DATABASE_NAME}' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: Failed to connect or execute command.")
        print(f"Details: {err}")

    finally:
        if mycursor:
            mycursor.close()
        if mydb and mydb.is_connected():
            mydb.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()