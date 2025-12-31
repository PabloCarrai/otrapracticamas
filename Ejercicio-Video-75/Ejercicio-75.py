#   Conexion a sqlserver
# pip install pyodbc

import pyodbc


try:
    conexion = pyodbc.connect(
        "DRIVER={SQL Server};SERVER=SERVIDOR;DATABASE=db1;UID=sa;PWD=M1longuita"
    )
    print("Conexion exitosa")
    cursor = conexion.cursor()
    cursor.execute("select @@version;")
    row = cursor.fetchone()
    print(row)
    cursor.execute("select * from tarea")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
except Exception as ex:
    print(f"Ocurrio algo con la conexion {ex}")
finally:
    conexion.close()
    print("Conexion finalizada")
