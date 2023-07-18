import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.64.2",
  user="crp_agent",
  password="",
  database="CRP"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
