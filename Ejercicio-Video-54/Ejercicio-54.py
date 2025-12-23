#   Map


def elevarCuadrado(num):
    return num * num


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))
print(numeros)
#numerosElevados = map(elevarCuadrado, numeros)
numerosElevados = list(map(elevarCuadrado, numeros))

print(numerosElevados)
