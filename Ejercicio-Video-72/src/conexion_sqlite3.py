import sqlite3

try:
    # conexion = sqlite3.connect(
    #     "/home/ed/otrapracticamas/Ejercicio-Video-72/src/database/miprimeradb"
    # )
    # cursor = conexion.cursor()
    # cursor.execute("create table persona(nombre varchar(50),edad integer)")

    conexion = sqlite3.connect(
        "/home/ed/otrapracticamas/Ejercicio-Video-72/src/database/misegundadb.sqlite"
    )
    cursor = conexion.cursor()
    cursor.execute("select * from productos")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

except Exception as ex:
    print(ex)

finally:
    conexion.close()
