def ejecutarOpcion(opcion):
    print(opcion)


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
