#   Archivos de texto
# file = open(
#     "/home/ed/otrapracticamas/Ejercicio-Video-60/data1.txt", "r"
# )  #   Abrimos el archivo para su lectura
# # print(file)
# lineas = file.readlines()  #   Devuelve una lista con el contenido del archivo
# print(lineas)
# file.close()  #   Lo cerramos

# with open("/home/ed/otrapracticamas/Ejercicio-Video-60/data2.txt", "r") as archivo:
#     lineas = archivo.readlines()
#     print(lineas)
# for l in lineas:
#     print(l.replace("\n", ""))  #   reemplazo los fines de linea por un espacio

# with open("/home/ed/otrapracticamas/Ejercicio-Video-60/data2.txt", "r") as archivo:
#     contenido = archivo.read()
#     lineas = contenido.split("\n")  #   Otra forma de quitar los fines de lineas
#     print(lineas)

# with open("/home/ed/otrapracticamas/Ejercicio-Video-60/data2.txt", "r") as archivo:
#     contenido = archivo.read()
#     lineas = contenido.split("\n")  #   Otra forma de quitar los fines de lineas
#     pos = archivo.tell()
#     print(pos)  #   Nos dice en que posicion de lectura estamos
#     print("El archivo tiene {0} caracteres de longitud".format(pos))

# with open("/home/ed/otrapracticamas/Ejercicio-Video-60/data2.txt", "r") as archivo:
#     archivo.seek(7)
#     pos = archivo.tell()
#     contenido = archivo.read()
#     lineas = contenido.split("\n")  #   Otra forma de quitar los fines de lineas
#     print("El archivo esta en la posicion {0}: ".format(pos))

# with open("/home/ed/otrapracticamas/Ejercicio-Video-60/data2.txt", "r") as archivo:
#     siguientes4 = archivo.read(7)
#     print(siguientes4)


# with open("/home/ed/otrapracticamas/Ejercicio-Video-60/data2.txt", "rb") as archivo:
#     print(type(archivo.read()))

with open("/home/ed/otrapracticamas/Ejercicio-Video-60/data3.txt", "w") as archivo:
    archivo.write("Pablo\nHernan\nJuan\nCarrai\nCavallaro")
