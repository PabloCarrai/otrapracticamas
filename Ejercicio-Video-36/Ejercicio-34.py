#   Herencia
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


#   Entre parentesis vemos de que Clase Hereda esta clase
class Estudiante(Persona):
    def __init__(
        self, apePat, apeMat, nom, pro
    ):  #   Estos son atributos del objeto hijo con los del padre
        super().__init__(apePat, apeMat, nom)  #   Estos son atributos del objeto padre
        self.profesion = pro


estu1 = Estudiante("Carrai", "Cavallaro", "Pablo", "Vago")
print(estu1.mostrarNombreCompleto())
print(estu1.profesion)
