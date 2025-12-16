#   polimorfismo(muchas formas)
class Estudiante:
    def describir(self):
        print("Soy un buen estudiante")


class Docente:
    def describir(self):
        print("Me dedico a enseñar cursos")


class Trabajador:
    def describir(self):
        print("Mis jefes son unos garcas")


def describirPersona(persona):
    persona.describir()


doc1 = Trabajador()

describirPersona(doc1)
