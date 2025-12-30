#   Conectar a mysql
import mysql.connector


try:
    conexion = mysql.connector.connect(
        host="192.168.0.222",
        port=3307,
        user="root",
        password="SomosDeCarn3",
        database="db1",
    )
    if conexion.is_connected():
        print("conexion exitosa")
        infoServer = conexion.get_server_info()
        print(infoServer)
        cursor = conexion.cursor()
        cursor.execute("select database()")
        row = cursor.fetchone()
        print(row)

except Exception as ex:
    print(ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("Conexion finalizada")
