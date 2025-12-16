#   Herencia, sobrescribir metodo
class Persona:
    def __init__(self, apePat, apeMat, nom):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = nom

    def mostrarNombreCompleto(self):
        txt = "{0} {1} {2} {3}"
        return txt.format(
            self.apellidoPaterno, self.apellidoMaterno, self.nombres, self.profesion
        )

    def datos(self):
        print(self.mostrarNombreCompleto())


#   Entre parentesis vemos de que Clase Hereda esta clase
class Estudiante(Persona):
    def __init__(
        self, apePat, apeMat, nom, pro
    ):  #   Estos son atributos del objeto hijo con los del padre
        super().__init__(apePat, apeMat, nom)  #   Estos son atributos del objeto padre
        self.profesion = pro

    def datos(
        self,
    ):
        super().datos()  #   Con esto reutilizo el datos original de la clase padre mas la de la clase hijo debajo
        print(
            "Profesion {0}".format(self.profesion)
        )  #   Si creo un metodo con el mismo nombre, sobrescribo el metodo original


estu1 = Estudiante("Carrai", "Cavallaro", "Pablo", "Vago")
estu1.datos()
