### PATRON DE DISEÑO FACTORY ###
# Esta variante incluye tanto un desacoplamiento de la creacion (con una interfaz)
# como un selector en runtime que va eligiendo que producto se crea

from abc import ABC, abstractmethod

# 1 - Se crean la interfaz de los productos

class IPersona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def que_soy(self):  # Metodo para comprobar la clase que se utiliza
        print(f'{self.nombre} es un {self.__class__.__name__.lower()}')
    
    @abstractmethod  # Metodo que representa la logica de cada producto
    def actividad(self):
        ...
        
# 2 - Se crean los productos

class Programador(IPersona):  # Los productos tienen la logica de los objetos
    def actividad(self):
        print(f'{self.nombre} esta programando')

class Politico(IPersona):
    def actividad(self):
        print(f'{self.nombre} esta engañando')
    
# 3 - Patron creacional fabrica (mezcla de variantes 1 y 2)

class IFPersona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        
    @abstractmethod
    def construir(self):
        ...
    
    def trabajar(self):
        persona = self.construir()
        persona.que_soy()
        persona.actividad()
class FProgramador(IFPersona):  # Fabricas concretas
    def construir(self):
        return Programador(self.nombre)
    
class FPolitico(IFPersona):
    def construir(self):
        return Politico(self.nombre)

if __name__ == '__main__':
    nombre = input("Nombre de la persona: ")
    trabajo = input("Trabajo de la persona: ")
    if trabajo.lower() == "programador":  # La eleccion no es en runtime, pero se ha desacoplado creacion y producto
        FProgramador(nombre).trabajar()
    elif trabajo.lower() == "politico":
        FPolitico(nombre).trabajar()
    else:
        raise TypeError("Ese trabajo no esta implementado")
