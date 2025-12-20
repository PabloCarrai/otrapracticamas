from BD.conexion import DAO
import funciones


def ejecutarOpcion(opcion):
    #   print(opcion)
    dao = DAO()
    if opcion == 1:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                funciones.listarCursos(cursos)
            else:
                print("No se encontraron cursos")
        except:
            print("Ocurrio un error al lista los cursos")
    elif opcion == 2:
        curso = funciones.pedirDatosRegistro()
        try:
            dao.registrarCurso(curso)
        except:
            print("Ocurrio un error al registrar un cursos")
        print("Registro")
    elif opcion == 3:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                curso = None
                if curso:
                    dao.actualizarCurso(curso)
                else:
                    print("codigo de curso a actualizar no encontrado")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrio un error con la actualizacion")

        print("Actualizacion")

    elif opcion == 4:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not (codigoEliminar == ""):
                    dao.eliminarCurso(codigoEliminar)
                else:
                    print("Codigo de curso no encontrado")
            else:
                print("No se encontraron cursos")
        except:
            print("Ocurrio un error al eliminar un cursos")
        print("Eliminacion")
    else:
        print("Opcion no valida")


def menuPrincipal():
    continuar = True
    while continuar:
        opcionCorrecta = False
        while not opcionCorrecta:
            print("Menu Principal:")
            print("1)- Listar Cursos")
            print("2)- Registrar Cursos")
            print("3)- Actualizar Cursos")
            print("4)- Eliminar Cursos")
            print("5)- Salir")
            opcion = int(input("Seleccione una opcion Valida: (1-2-3-4-5):   "))
            if opcion < 1 or opcion > 5:
                print("Opcion Incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("Gracias por usar el sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


menuPrincipal()
