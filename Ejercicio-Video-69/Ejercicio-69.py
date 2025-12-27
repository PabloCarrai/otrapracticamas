# Interfaces
from abc import ABC, abstractmethod  # crea clases abstractas


#   Creo la clase abstracta y sus metodos abstractos
class MyInterface(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass


class ClassA(MyInterface):
    def method1(self):
        print("ClaseA method1")

    def method2(self):
        print("ClaseA method2")


class ClassB(MyInterface):
    def method1(self):
        print("ClaseB method1")

    def method2(self):
        print("ClaseB method2")


objA = ClassA()
objA.method1()
objB = ClassB()
objB.method1()