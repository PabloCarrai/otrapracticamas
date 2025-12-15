#   Excepciones
numero1 = 20
numero2 = 2
#   No se puede dividir por 0, por eso da error
# print("La division de {0} entre {1} es:{2} ".format(numero1, numero2, (numero1 / numero2)))

#   Se intenta hacer algo
try:
    resultado = numero1 / numero2
#   Si falla tomamos una medida pero el programa continua, no se interrumpe
except ZeroDivisionError:
    print("No es posible dividir entre 0...")
#   Esto de abajo se ejecuta siempre
finally:
    print("Yo siempre aparezco")


#   El existir un error anterior, esta parte ya no se ejecutaria
print("Aqui termina el programa")
