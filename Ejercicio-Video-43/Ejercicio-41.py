import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="192.168.0.222",
        user="root",
        password="SomosDeCarn3",
        database="db1",
        port="3307",
    )
    if connection.is_connected():
        print("Conexion Exitosa")
        infoServer = connection.get_server_info()
        print(f"Info del server {infoServer}")

except Error as ex:
    print(f"Error durante la conexion: {ex}")

finally:
    if connection.is_connected():
        connection.close()
        print("Conexion finalizada")
