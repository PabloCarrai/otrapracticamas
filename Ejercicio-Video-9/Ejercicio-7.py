"""
Tupla
"""

tupla = (1, 2, 3)
print(tupla)
tupla2 = (7, "Oscar", True, 450.1, 16 + 7j, "Felicidad", False)
print(tupla2)
tupla3 = (9, 3, (4, 5, 6))
print(tupla3)
#   accediendo a Oscar
print(tupla2[1])
#   No se puede modificar un valor en la tupla(no se puede modificar la tupla en si)
# tupla2[1]="Pirulo"
#   Accede al ultimo elemento de la tupla
print(tupla2[-1])
#   Imprimo de la tupla 2 los elementos desde la posicion 0 a la 4(sin incluir)
print(tupla2[0:4])
#   Muestra desde el segundo ultimo elemento
print(tupla2[-2])
#   Asignamos los valores de la tupla a unas variables
a, b, c = tupla
print(a, b, c)
#   Podemos crear una tupla a partir de la suma de dos tuplas diferentes
tuplaFinal = tupla + tupla3
print(tuplaFinal)
#   Contamos las veces que tenemos un 3 en tuplafinal
print(tuplaFinal.count(3))
#   Nos indica la posicion de un elemento, la primer aparicion.
print(tuplaFinal.index(3))
