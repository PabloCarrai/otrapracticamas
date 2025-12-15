#   Encapsulamiento, es esconder/ocultar una funcion(metodo)/propiedad del objeto


class Curso:
    """nombre="Matematica"
    creditos=5
    profesion="Ingenieria Civil"
    """

    #   Constructor de la clase, inicializadora de la misma
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial"  #   Propiedad Encapsulada

    def mostrarDatos(self):
        dat = "Nombre: {0} / Creditos: {1} / Modo de imparticion: {2}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))


curso1 = Curso(
    "Pedro Marmol de Lepizioni del Turgentino Maccardista", 12, "Ingenieria Civil"
)
print(curso1.nombre)
#   Esta ya no es la propiedad existente, sino una creada en este momento
# curso1.imparticion = "Virtual"
# print(curso1.imparticion)
curso1.mostrarDatos()

#    Instanciamos otro objeto
# curso2 = Curso("Yesica del Alba Instricschescovich Marronis", 5, "Youtuber")
# print(curso2.nombre)
