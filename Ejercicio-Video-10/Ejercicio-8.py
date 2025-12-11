"""
Listas
"""

#   Crea la lista con tres elementos
lista = ["Oscar", 25, 98.3, True, "Flavio", 56.3]
#   Imprime la lista
print(lista)
#   Otra forma de imprimir completa la lista
print(lista[:])
#   Un solo elemento en especifico
print(lista[2])
#   Ultimo elemento
print(lista[-1])
#   Accediendo a una cantidad de elementos de la lista(0 a 3 sin incluirlo)
print(lista[0:3])
#   Otra forma pero desde 0 hasta 2(sin incluirlo)
print(lista[:2])
#   Otra forma, pero desde una posicion hasta el final
print(lista[3:])
#   Agregar al final de la lista un elemento
lista.append("Los Flacos Huerfanos")
print(lista)
#   Agregar en una posicion determinada un elemento
lista.insert(4, "Laurita")
print(lista)
#   Otra forma de agregar elementos, es con extend
lista.extend(["Flavia", "Yesica", "Romina"])
print(lista)
#   Obtener el indice de un elemento
print(lista.index("Romina"))
#   Eliminar un elemento de la lista
lista.remove(56.3)
print(lista)
#   Otra forma es usar pop(elimina el ultimo elemento de la lista)
lista.pop()
print(lista)
#   Union de listas
lista2 = ["Roberto", "Miranda"]
lista3 = lista + lista2
print(lista3)
#   Mostrar varias veces una lista
print(lista2 * 4)
#   Verificar si un elemento esta en la lista
print("Yesica" in lista)
