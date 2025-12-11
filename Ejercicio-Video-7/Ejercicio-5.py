#   Concatenacion
#   1er Forma
texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2
print(textoFinal)

#   2da forma
print("El saludo es %s %s" % (texto1, texto2))

#   3ra forma
saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
print(saludoFinal)

#   4ta forma
saludoFinal2 = "Saludo: {x} {y}".format(x=texto1, y=texto2)
print(saludoFinal2)
