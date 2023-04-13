import mysql.connector as con

db = con.connect(
    host="localhost",
    user="root",
    password="password1234",
    database="employee",
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
  ("Shakib", "Magura"),
  ("Tamin", "Ctg"),
  ("Taskin", "Dhaka"),
  ("Mushfiq", "Rajshahi")
]

for val in values:
  cursor.execute(sql, val)

db.commit()

print("{} data added".format(cursor.rowcount))
