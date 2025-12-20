import mysql.connector
from mysql.connector import Error


class DAO:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="192.168.0.222",
                user="root",
                password="SomosDeCarn3",
                database="universidad",
                port="3307",
            )
        except Error as ex:
            print(f"Error al intentar la conexion {ex}")

    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select * from curso order by nombre asc")
                resultado = cursor.fetchall()
                return resultado
            except Error as ex:
                print(f"Error al listar Cursos(listarCursos) {ex}")
            finally:
                self.conexion.close()
