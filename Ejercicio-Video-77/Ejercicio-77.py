from db import get_connection


try:
    conexion = get_connection()
    with conexion.cursor() as cursor:
        id = 3
        cursor.execute(
            "select codigo,descripcion,precio from articulos where codigo=%s", (id,)
        )
        row = cursor.fetchone()
        print(row)
    conexion.close()
except Exception as ex:
    print(ex)
