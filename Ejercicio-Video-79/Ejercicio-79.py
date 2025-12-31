from db import get_connection
from random_data import data


try:
    conexion = get_connection()
    print(conexion)
    cursor = conexion.cursor()
    cursor.executemany(
        """insert into person(id,name,company,job,email,phone,mac_address)values(%s,%s,%s,%s,%s,%s,%s)""",
        data,
    )
    if len(data) == cursor.rowcount:
        conexion.commit()
        print(f"{len(data)} rows inserted.")
    else:
        conexion.rollback()  #   Esto en caso de que lo anterior falla hacer un rollback
except Exception as ex:
    print(f"Error durante la conexion {ex}")
finally:
    conexion.close()
    print("Conexion Cerrada")
