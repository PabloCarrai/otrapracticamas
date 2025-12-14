#   Factorial de un numero
numero = int(input("Numero? "))
factorial = 1
for n in range(1, (numero + 1)):
    factorial = factorial * n
print("Factorial de {0} es :{1}".format(n, factorial))
