#   Break
for numero in range(1, 6):
    if numero == 3:
        break  #   Esto sale del bucle cuando numero sea igual a 3
    print("El numero es {0}".format(numero))
print("Bucle terminado")
#   Continue
for numero in range(1, 6):
    if numero == 3:
        continue  #   quita una iteracion y continua al proximo
    print("El numero es {0}".format(numero))
print("Bucle terminado")
#   Pass
for numero in range(1, 6):
    if numero <= 3:
        pass  #   No pasa nada
    else:
        print("El siguiente valor es {0} es mayor a 3".format(numero))
    print("El numero es {0}".format(numero))
print("Bucle terminado")
