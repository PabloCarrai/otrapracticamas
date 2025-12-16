#   Relaciones de clases
class Pais:
    def __init__(self, nom, pre):
        self.nombre = nom
        self.presidente = pre

    def __str__(self):
        txt = "Pais: {0}, Presidente: {1}"
        return txt.format(self.nombre, self.presidente)


class Ciudad:
    def __init__(self, nom, hab, pai):
        self.nombre = nom
        self.habitantes = hab
        self.pais = pai

    def __str__(self):
        txt = "Ciudad: {0} - N Habitantes: {1}, ({2})"
        return txt.format(self.nombre, self.habitantes, self.pais)


class Urbanizacion:
    def __init__(self, nom, ciu):
        self.nombre = nom
        self.ciudad = ciu

    def __str__(self):
        txt = "Urbanizacion: {0}, (Ciudad: {1})"
        return txt.format(self.nombre, self.ciudad)


mexico = Pais("Mexico", "Martin Vizcarra")
print(mexico)
ciudad1 = Ciudad(
    "Chiclayo", 1500000, mexico
)  # La relacion esta al recibir una instancia de Pais(mexico), y ahi se vincula
print(ciudad1)

urbanizacion = Urbanizacion("chihuahua", mexico)
print(urbanizacion)
