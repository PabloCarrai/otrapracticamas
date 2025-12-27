#   Decoradores
#   modifican methodos sin alterar el codigo original
#   Usan una funcion y la devuelven modificada


def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar mi_funcion")
        resultado = func(*args, **kwargs)
        print("Despues de ejecutar mi_funcion")
        return resultado

    return wrapper


@mi_decorador  # Es esto
def mi_funcion():
    print("Esta es mi funcion")


mi_funcion()
