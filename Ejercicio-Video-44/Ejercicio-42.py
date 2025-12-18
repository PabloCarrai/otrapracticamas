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
        cursor.execute("select database();")
        resultado = cursor.fetchone()
        print(f"Conectado a la DB:{resultado}")
        cursor.execute("select * from articulos")
        resultados = cursor.fetchall()
        for e in resultados:
            print(f"Codigo: {e[0]} Producto: {e[1]} Precio: {e[2]}")
        print(f"Total de Registro: {cursor.rowcount}")

except Error as ex:
    print(f"Error durante la conexion: {ex}")

finally:
    if connection.is_connected():
        connection.close()
        print("Conexion finalizada")
