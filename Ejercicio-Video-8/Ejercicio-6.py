#   Manejo de cadenas
texto = "Bienvenidos al canal de AndaAsaber"
print(texto)  #   Muestra el original
print(texto.lower())  #   Transforma a caracter en minuscula
print(texto.upper())  #   Transforma a caracter en mayusculas
print(
    texto.title()
)  #   Transforma el primer caracter de cada palabra en mayuscula(como un titulo)
print(texto.find("al"))  #   Busca al en la palabra y devuelve el indice de la posicion
print(texto.count("e"))  #   cuenta las apariciones de un string
textoFinal = texto.replace(
    "e", "3"
)  #  Reemplaza el primer string con el segundo en todo el string original
print(textoFinal)

valor = texto.isnumeric()  #  Revisa si lo que guarda texto es un numero
print(valor)

cadenaSeparada = texto.split(
    " "
)  #   Genera una lista con los elementos del texto separando por el elemento del split, aca es por espacio
print(cadenaSeparada)
