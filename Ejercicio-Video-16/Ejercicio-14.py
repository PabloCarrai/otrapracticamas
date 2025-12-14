#   Operador ternario

sexos = ("Hombre", "Mujer")
posicion = True
sexo = sexos[posicion]  # Mujer
print(sexo)
sexo = sexos[not posicion]  # Hombre
print(sexo)
#   Ahi va el ejemplo
sexo = "Masculino" if posicion == True else "Femenino"
print(sexo)
