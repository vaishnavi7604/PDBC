import mysql.connector

def db_Connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vaishu@07",
        database="HDFCBank"
    )

print("WELCOME TO HDFC BANK !")
