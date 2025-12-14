#   Ingreso de datos por teclado
nombre = "Daniel"
edad = 22
print("Hola " + nombre)
print("Tu edad es : ", edad)
print("##################################")
#   Mismo ejemplo pero ingresando ambos valores
nombre = input("Ingrese su Nombre: ")
edad = input("Ingrese su Edad: ")
print("Hola " + nombre)
print("Tu edad es : ", edad)
print("##################################")
#   Usando edad futura
nombre = input("Ingrese su Nombre: ")
#   Input devuelve string, con int lo convierto a entero
edad = int(input("Ingrese su Edad: "))
edadFutura = edad + 20
sueldo = float(input("Ingresa tu sueldo: "))
print("Hola " + nombre)
print("Tu edad es : ", edad)
print("Tu edad dentro de 20 años sera : ", edadFutura)
print("Ganas ", sueldo)
