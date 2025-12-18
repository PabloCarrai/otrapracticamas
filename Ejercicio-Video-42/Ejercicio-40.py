import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_database = os.getenv("DB_DATABASE")
db_port = os.getenv("DB_PORT")


connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_pass,
    database=db_database,
    port=db_port,
)

cursor = connection.cursor()
cursor.execute("select * from articulos;")
resultado = cursor.fetchall()
for linea in resultado:
    print(linea)
cursor.close()
connection.close()
