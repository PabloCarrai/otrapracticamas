#   Raise
def evaluarNota(nota):
    if nota < 0:
        #  Creo una excepcion utilizando ya una existente, pero con mensaje propio
        # raise ZeroDivisionError(
        #     "No se permite valores negativo..."
        # )
        # Otro ejemplo
        raise ValueError("Valor Incorrecto...")
    elif nota >= 16:
        print("Excelente")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Desaprobado")


evaluarNota(13)
evaluarNota(-1)
