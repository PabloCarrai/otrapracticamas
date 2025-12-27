# heapq
import heapq

numbers = [1, 4, 2, 100, 20, 750, 50, 32, 150, -500, 8]
resultado = heapq.nlargest(3, numbers)  # de un iterable devuelve n numeros mayores
print(resultado)
print(type(resultado))

resultado2 = heapq.nsmallest(2, numbers)
print(resultado2)
print(type(resultado2))
