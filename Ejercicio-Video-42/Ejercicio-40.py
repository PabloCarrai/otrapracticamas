import mysql.connector

connection = mysql.connector.connect(
    host="192.168.0.222",
    user="root",
    password="SomosDeCarn3",
    database="db1",
    port="3307"
)


cursor = connection.cursor()
cursor.execute("select * from articulos;")
resultado = cursor.fetchall()
for linea in resultado:
    print(linea)
cursor.close()
connection.close()
