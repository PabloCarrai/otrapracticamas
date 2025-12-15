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


curso1 = Curso(
    "Pedro Marmol de Lepizioni del Turgentino Maccardista", 12, "Ingenieria Civil"
)
print(curso1.nombre)

#   Instanciamos otro objeto
curso2 = Curso("Yesica del Alba Instricschescovich Marronis", 5, "Youtuber")
print(curso2.nombre)
