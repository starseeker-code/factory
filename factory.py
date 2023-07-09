### PATRON DE DISEÑO FACTORY ###
# Esta variante va creando los productos en runtime, pero no tiene
# unas clases creadoras, simplemente tiene una clase fabrica

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
    
# 3 - Patron creacional fabrica

def Fabrica(nombre, trabajo):
    match trabajo.lower():
        case 'programador':
            __instancia = Programador(nombre)
        case 'politico':
            __instancia = Politico(nombre)
        case _ :
            raise TypeError("No se ha implementado ese trabajo")
    __instancia.que_soy()
    __instancia.actividad()

if __name__ == '__main__':
    nombre = input("Nombre de la persona: ")
    trabajo = input("Trabajo de la persona: ")
    Fabrica(nombre, trabajo)  # Se crea el objeto en runtime, pero no hay objetos creadores, la fabrica es una funcion selectora
