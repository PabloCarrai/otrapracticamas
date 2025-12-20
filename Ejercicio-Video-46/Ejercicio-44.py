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
        cursor.execute(
            "update usuarios set direccion='Miguelete 457',telefono='1540809423',nombre='Juan Miguelete' where id_usuario=11 "
        )
        connection.commit()
        print("Registro Actualizado con exito")

except Error as ex:
    print(f"Error durante la conexion: {ex}")

finally:
    if connection.is_connected():
        connection.close()
        print("Conexion finalizada")
