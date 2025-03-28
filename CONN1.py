import mysql.connector
def mycon():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Charan@123",
        database="wfm"
    )
    return mydb
