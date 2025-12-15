#   Primer forma de importar
# import modulo1
# print(modulo1.multiplicar(7, 8))
# print(modulo1.restar(17, 8))
# print(modulo1.dividir(27, 8))
# print(modulo1.sumar(7, 8))

# 2 forma
from modulo1 import sumar, multiplicar, dividir, restar
from mi_paquete.funciones_matematicas import calcular_factorial, frase
from mi_paquete.sub_paquete1.funciones_avanzada import contar_letras

print(sumar(3, 4))
print(dividir(45, 6))
print(multiplicar(883, 56))
print(calcular_factorial(23))
print(frase)
texto = "Gracias por no ser un sorete/a"
print(contar_letras(texto))
