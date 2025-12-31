#   Oracle
#    pip install cx_Oracle

import cx_Oracle

try:
    conexion = cx_Oracle.connect(
        user="candia",
        password="candia",
        dsn="192.168.0.222:1521/XEPDB2",
        encoding="UTF-8",
    )
    print(conexion.version)
    cursor = conexion.cursor()
    cursor.execute("select * from sucursal")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(f"Ocurrio un error al conectarse {ex}")

finally:
    conexion.close()
    print("Conexion Finalizada...")
