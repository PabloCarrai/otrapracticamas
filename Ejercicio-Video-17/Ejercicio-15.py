#   Comparacion en if mediante el operador in
print("-- Cursos --")
print("Matematicas - Biologia - Lenguaje - Ciencias")

curso = input("Ingrese curso deseado ")

if curso in ("Matematicas", "Biologia", "Lenguaje", "Ciencias"):
    print("Curso {0} Seleccionado. ".format(curso))
else:
    print("No existe ese curso..")
