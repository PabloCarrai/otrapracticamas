#   Generadores
def generaMultiplos7(limite):
    numero = 1
    listaNumeros = []
    while numero <= limite:
        listaNumeros.append(numero * 7)
        numero += 1
    return listaNumeros


print(generaMultiplos7(10))


#   Ejemplo con generadores
def generadorMultiplos7(limites):
    numeros = 1
    while numeros <= limites:
        yield numeros * 7  # genera un objeto iterable
        numeros += 1


obtienemultiplo7 = generadorMultiplos7(10)
# for e in obtienemultiplo7:
#     print(e)

#   next() devuelve proximo elemento de un objeto iterable
print(next(obtienemultiplo7))
#   next() devuelve proximo elemento de un objeto iterable
print(next(obtienemultiplo7))
#   next() devuelve proximo elemento de un objeto iterable
print(next(obtienemultiplo7))