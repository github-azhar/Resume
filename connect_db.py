import mysql.connector as con

db = con.connect(
    host="localhost",
    user="root",
    password="password1234"
)

if db.is_connected():
    print("Database Connected")
