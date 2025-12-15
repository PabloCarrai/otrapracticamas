#   Encapsular una funcion(Methodo) en una clase
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
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print("Existe docente Asignado...")
        else:
            print("No es necesario asignar un docente...")

    def __verificarDocente(self):
        print("Verificando si existe docente asignado...")
        #   Que locura jajajaja
        return True if self.__imparticion == "Presencial" else False


curso1 = Curso(
    "Pedro Marmol de Lepizioni del Turgentino Maccardista", 12, "Ingenieria Civil"
)
print(curso1.nombre)
curso1.mostrarDatos()
