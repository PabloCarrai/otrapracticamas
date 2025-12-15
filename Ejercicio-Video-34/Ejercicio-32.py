class Cuenta:
    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon

    #   Metodos getters(metodo gets) se usan para setear o obtener valores de metodos/propiedades encapsulada
    def get_saldo(self):
        return self.__saldo

    def get_moneda(self):
        return self.__moneda

    def get_propietario(self):
        return self.__propietario

    #   Metodos Setters(metodo sets) se usan para setear o obtener valores de metodos/propiedades encapsulada
    def set_moneda(self, moneda):  #   Paso por parametro el nuevo valor de la moneda
        self.__moneda = moneda


cuenta1 = Cuenta("Daniela Mendez", 25000, "Soles")
print(cuenta1.get_saldo())
print(cuenta1.get_moneda())
cuenta1.set_moneda("Dolares")
print(cuenta1.get_moneda())
