### PATRON DE DISEÑO FACTORY ###

from abc import ABC, abstractmethod

# 1 - Se crean la interfaz de los productos

class IPersona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def que_soy(self):
        print(f'{self.nombre} es un {self.__class__.__name__.lower()}')
    
    @abstractmethod
    def actividad(self):
        ...
        
# 2 - Se crean los productos

class Programador(IPersona):
    def actividad(self):
        print(f'{self.nombre} esta programando')

class Politico(IPersona):
    def actividad(self):
        print(f'{self.nombre} esta engañando')
    
# 3 - Patron creacional fabrica (mezcla de variantes 1 y 2)

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def asignar_trabajo(self, trabajo):
        match trabajo.lower():
            case "programador":
                __instancia = FProgramador(nombre)
            case "politico":
                __instancia = FPolitico(nombre)
            case _ :
                raise TypeError('No se tiene ese trabajo')
        __instancia.trabajar()
        
    def trabajar(self):
        persona = self.construir()
        persona.que_soy()
        persona.actividad()

class FProgramador(Persona):
    def construir(self):
        return Programador(self.nombre)
    
class FPolitico(Persona):
    def construir(self):
        return Politico(self.nombre)

if __name__ == '__main__':
    nombre = input("Nombre de la persona: ")
    trabajo = input("Trabajo de la persona: ")
    Persona(nombre).asignar_trabajo(trabajo)
