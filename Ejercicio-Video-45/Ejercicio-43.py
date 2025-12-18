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
        nombre = input("Ingresa tu nombre:  ")
        direccion = input("Tu direccion? ")
        telefono = input("Telefono?")
        sentencia = "insert into usuarios(nombre,direccion,telefono) values('{0}','{1}','{2}')".format(
            nombre, direccion, telefono
        )
        cursor.execute(sentencia)
        connection.commit()
        print("Registro insertado con exito")

except Error as ex:
    print(f"Error durante la conexion: {ex}")

finally:
    if connection.is_connected():
        connection.close()
        print("Conexion finalizada")
