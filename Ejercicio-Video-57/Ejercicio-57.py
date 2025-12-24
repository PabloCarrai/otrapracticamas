# Math
import math

x = 1.053
print(round(x))
print(round(x, 1))
print(math.ceil(x))  #   Redondeo pa arriba
print(math.floor(x))  #   Redondeo pa abajo
print(math.trunc(x))  # retorna parte entera de un decimal
numeros = [1, 2, 3, 4, 5]
print(int(math.fsum(numeros)))  # Suma de todos los elementos de un iterable
print(math.fabs(-4))  #   Valor absoluto
print(math.fmod(17, 6))  #    Devuelve el modulo de dos digitos
print(math.exp(2))  #   Retorna epsilon elevado al cuadrado
print(math.pi)  #   Retorna el valor de pi
print(math.pow(5, 6))  #   Eleva a potencia 5 a la 6
print(math.sqrt(16))  #   Raiz cuadrada de 16
h = math.hypot(1.5, 1.5)  # calcula la hipotenusa de un triangulo
print(h)
r = math.radians(45)  # valores en radianes
print("Valor en radianes: {0}".format(r))
print(math.sin(47))  #   veo el seno de 47
print(math.remainder(16, 2))  #    Residuo
