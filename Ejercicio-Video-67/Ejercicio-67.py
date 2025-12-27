from db import get_connection

# try:
#     connection = get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute(
#             "select * from articulos"
#         )  #   No tengo procedimientos vamos con un listado de tabla
#         resultadoset = cursor.fetchall()
#         for row in resultadoset:
#             print(f"Codigo: {row[0]} Descripcion: {row[1]} Precio:{row[2]}")
#         connection.close()
# except Exception as ex:
#     print(ex)


try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            "select * from articulos where codigo=%s", (37,)
        )  #   No tengo procedimientos vamos con un listado de tabla
        resultadoset = cursor.fetchall()
        for row in resultadoset:
            print(f"Codigo: {row[0]} Descripcion: {row[1]} Precio:{row[2]}")
        connection.close()
except Exception as ex:
    print(ex)
