#   Diccionarios
miDiccionario = {"España": "Madrid", "Peru": "Lima", "Alemania": "Berlin"}
print(miDiccionario["Peru"])  # Mediante la clave accedo al valor
print(miDiccionario)  #   Imprimo el diccionario completo
#   Agregar un elemento
miDiccionario["Venezuela"] = "Caracas"
print(miDiccionario)
miDiccionario["España"] = (
    "Barcelona"  # Si la clave existe, se reemplaza el valor con el nuevo valor
)
print(miDiccionario)
#   Eliminar un valor de un diccionario
del miDiccionario["España"]
print(miDiccionario)
dic2 = {"Garcia": "Oscar", 25: True, "Sueldo": 150.80}
print(dic2)
print(dic2[25])  #   Accedo al valor de la clave 25 qie es True
#   Otra forma de crear un diccionario
llaves = ("España", "Francia", "Inglaterra")
dicPaises = {llaves[0]: "Madrid", llaves[1]: "Paris", llaves[2]: "Londres"}
print(dicPaises)
#   Diccionario con elementos de diccionarios
datosPersonales = {
    "Apellido": "Garcia",
    "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014},
}
print(datosPersonales)
#   Acceder a los valores de anios
print(datosPersonales["Anios"])
#   Busca un valor y si no lo encuentra devuelve el segundo parametro
print(datosPersonales.get("Ape", "Oscar"))
#   Aca lo encuentra y devuelve
print(datosPersonales.get("Apellido", "Oscar"))
#   Para ver las llaves de nuestro diccionario
print(datosPersonales.keys())
#   Para ver los valores de las llaves
print(datosPersonales.values())
#   Convierto en una lista los valores del diccionario datospersonales
valores = list(datosPersonales.values())
#   Imprimo la lista
print(valores)
