"""
#   set
canasta = {"manzana", "platano", "pera", "manzana", "naranja", "pera"}
print(canasta)


numeros = {1, 3, 5, 8, 3, 4, 12, 1}
print(numeros)

#   Estos son mutables(pueden cambiar)
a = set("abracadabra")
print(a)
a.add("g")
print(a)
a.add("a")
print(a)
#   Vamos con los que no pueden cambiar
b = frozenset("perro")
print(b)
b.add("Sali")  # tira error
print(b)

"""

#   Obtengo los comunes de ambos
# miSet = {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}  # igual a miSet = {1, 2, 3, 4, 5} & {3, 4, 5, 6}

#   Union es la suma de ambos sin repetir
# miSet = {1, 2, 3, 4, 5}.union({3, 4, 5, 6})
# miSet = {1, 2, 3, 4, 5} | {3, 4, 5, 6}

#   Diferencia
# miSet = {1, 2, 3, 4, 5}.difference({2, 3, 5})
# miSet = {1, 2, 3, 4, 5} - {2, 3, 5}

#   Diferencia simetrica
# miSet = {1, 2, 3, 4, 5}.symmetric_difference({2, 3, 5})

# miSet = {1, 2, 3, 4, 5}.issuperset({1, 2, 3})
# miSet = {1, 2, 3, 4, 5}.issubset({1, 2, 3})

# print(miSet)
