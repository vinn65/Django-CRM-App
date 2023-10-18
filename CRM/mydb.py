import mysql.connector

db1 = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "PASS123",
    
)

cursorObject = db1.cursor()
cursorObject.execute("CREATE DATABASE mydb")
print("DONE!")