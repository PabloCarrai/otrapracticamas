#   Conexion a postgresql
#   pip install psycopg2

import psycopg2

try:
    conexion = psycopg2.connect(
        host="192.168.0.222",
        user="tu_usuario",
        password="tu_contraseña_segura",
        database="mi_base_de_datos",
        port=5432,
    )
    print("Conexion Exitosa")
    cursor = conexion.cursor()
    cursor.execute("select version()")
    row = cursor.fetchone()
    print(f"Version: {row}")
except Exception as ex:
    print(ex)
