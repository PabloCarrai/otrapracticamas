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
        cursor = connection.cursor()
        cursor.execute("delete from usuarios where id_usuario=12 ")
        connection.commit()
        print("Registro Eliminado con exito")

except Error as ex:
    print(f"Error durante la conexion: {ex}")

finally:
    if connection.is_connected():
        connection.close()
        print("Conexion finalizada")
