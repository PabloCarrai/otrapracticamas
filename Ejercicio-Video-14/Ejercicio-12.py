#   Funciones


def saludar():
    print("Pablo")
    print("Carrai")
    return "Hola "


saludar()
saludar()
saludar()
saludar()
print(saludar())


def evaluarSueldoMinimo(sueldo):
    if sueldo >= 850:
        print("Cumples con el sueldo")
    else:
        print("Ganas menos que el minimo")

evaluarSueldoMinimo(1200)
evaluarSueldoMinimo(12)
evaluarSueldoMinimo(int(input("Sueldo? ")))
