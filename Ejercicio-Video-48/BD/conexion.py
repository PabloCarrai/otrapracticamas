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

    def registrarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = (
                    "insert into curso(Codigo,Nombre,Creditos)values('{0}','{1}','{2}')"
                )
                cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print("Curso registrado")
            except Error as ex:
                print(f"Error al registrar Cursos(registrarCurso) {ex}")
            finally:
                self.conexion.close()

    def actualizarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "update curso set Nombre='{0}',Creditos='{1}' where Codigo='{2}'"
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print("Curso actualizado")
            except Error as ex:
                print(f"Error al registrar Cursos(actualizarCurso) {ex}")
            finally:
                self.conexion.close()

    def eliminarCurso(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "delete from curso where codigo='{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("Curso Eliminado")
            except Error as ex:
                print(f"Error al eliminar Cursos(eliminarCurso) {ex}")
            finally:
                self.conexion.close()
