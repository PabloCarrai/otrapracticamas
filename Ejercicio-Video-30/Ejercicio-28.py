#   Definimos el objeto persona
class Persona:
    #   Propiedades,caracteristica,atributo
    apellido = ""
    nombre = ""
    edad = 0
    despierto = False

    #   funcionalidad(Metodo)
    def despertar(self):
        #   Llamo a un atributo para cambiar su valor
        self.despertar = True
        print("Buen dia")


#   Instanciamos al objeto
persona1 = Persona()
#   Definimos el atributo apellido
persona1.apellido = "Garcia"
#   Lo imprimimos
print(persona1.apellido)
persona1.despertar()
print(persona1.despierto)


#   Creamos otra instancia del mismo objeto
#   Instanciamos al objeto
persona2 = Persona()
#   Definimos el atributo apellido
persona2.apellido = "Sanchez"
#   Lo imprimimos
print(persona2.apellido)
# persona2.despertar()
print(persona2.despierto)
