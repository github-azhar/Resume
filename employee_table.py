import mysql.connector as con

db = con.connect(
    host="localhost",
    user="root",
    password="password1234",
    database="employee",
)

cursor = db.cursor()
sql = """CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address Varchar(255)
)
"""
cursor.execute(sql)

print("Table Created Successful !!!")
