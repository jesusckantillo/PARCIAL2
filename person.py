from abc import ABC
from abc import abstractmethod
from typing import List
from main import Imperium
#Person and people classes
class Person(ABC):
    
    ID = 000000

    def __init__(self, name: str,planet:Planet)->None:
        self._name: str = name
        self._id_string: str  = str(Person.ID+1)
        self._planet: "Planet" = planet ##Mandar planeta como diccionario
        

class Soldier(Person):

    def __init__(self, name: str, age: int, planet: Planet) -> None:
        super().__init__(name,planet)
        self.__age = age

class Bureaucrat(Person):
    
        def __init__(self, name: str, deparment: str, planet: Planet) -> None:
            super().__init__(name, planet)
            self.__department: str = None


class Astarte(Person):
     def  __init__(self, name: str, founding: int, planet: Planet) -> None:
          super().__init__(name, planet)
          self.__founding: int = founding


class Primarch(Person):
     
     def __init__(self, name: str,  alias: str, planet: Planet) -> None:
          super().__init__(name, planet)
          self.__alias: str = alias
          self.__loyalty: bool = True
          self.__status: enumerate = Status.Alive
          self.__imperium: "Imperium" = Imperium

     def betray(self) -> None:
        self.__loyalty = False

     def change_status(self, status: enumerate) -> None:
        self.__status = status 