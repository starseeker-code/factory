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

class Persona:  # Interfaz que combina tanto la logica (trabajar) como la creacion (asignar_trabajo) y desacopla seleccion
    def __init__(self, nombre):
        self.nombre = nombre
    
    def asignar_trabajo(self, trabajo):  # Selecciona en runtime la fabrica concreta, que creara el producto concreto
        match trabajo.lower():
            case "programador":
                __instancia = FProgramador(nombre)
            case "politico":
                __instancia = FPolitico(nombre)
            case _ :
                raise TypeError('No se tiene ese trabajo')
        __instancia.trabajar()  # Ejecuta la logica (en este caso acoplado, se puede desacoplar)
        
    def trabajar(self):  # Logica, que se utiliza desde los productos
        persona = self.construir()
        persona.que_soy()
        persona.actividad()

class FProgramador(Persona):  # Fabricas concretas
    def construir(self):
        return Programador(self.nombre)
    
class FPolitico(Persona):
    def construir(self):
        return Politico(self.nombre)

if __name__ == '__main__':
    nombre = input("Nombre de la persona: ")
    trabajo = input("Trabajo de la persona: ")
    Persona(nombre).asignar_trabajo(trabajo)
