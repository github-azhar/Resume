import mysql.connector as con

db = con.connect(
    host="localhost",
    user="root",
    password="password1234",
    database="employee",
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Mr Taif", "Dhaka")
cursor.execute(sql, val)

db.commit()

print("{} data added".format(cursor.rowcount))
