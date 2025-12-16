#   funcion str tostring
class Curso:
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

    def __str__(
        self,
    ):  # Muestra un texto por defecto cuando se llama al objeto instanciado sin usar metodos o propiedades
        #   Muestra texto a mostrar cuando se accede  a un objeto puramente
        texto = "Nombre: {0} - Creditos: {1}"
        return texto.format(self.nombre, self.creditos)


curso1 = Curso(
    "Pedro Marmol de Lepizioni del Turgentino Maccardista", 12, "Ingenieria Civil"
)
print(
    curso1
)  #   Aca estaria el uso de __str__ llamo el objeto sin usar metodo/atributo alguno
print(curso1.nombre)
curso1.mostrarDatos()
