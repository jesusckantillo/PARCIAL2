from __future__ import annotations
from abc import ABC
from utils.enum import Status
from typing import List
from core.imperium.planets import Planet

#Person and people classes
class Person(ABC):
    
    last_id = -1

    def __init__(self, name: str, planet: "Planet") -> None:
        self._name: str = name
        self._id_string: str = Person.gen_id()
        self._planet: "Planet" = planet

    @staticmethod
    def gen_id():
        Person.last_id += 1
        return format(Person.last_id, '06x')
    
class Soldier(Person):

    def __init__(self,name:str,age:int, planet_info:dict) -> None:
        super().__init__(name,planet_info)
        self.__age = age

class Bureaucrat(Person):
    
        def __init__(self, name: str, deparment: str, planet: Planet) -> None:
            super().__init__(name, planet)
            self.__department: str = None

        def set_planet(self, planet: Planet) -> None:
            self._planet = planet

        @property
        def name(self) -> str:
            return self._name
        @property
        def id_string(self) -> str:
            return self._id_string

class Astarte(Person):
     def  __init__(self, name: str, founding: int, planet: Planet) -> None:
          super().__init__(name, planet)
          self.__founding: int = founding


class Primarch(Person):
     
     def __init__(self, name: str,  alias: str, planet: Planet) -> None:
          super().__init__(name, planet)
          self.__alias: str = alias
          self.__loyalty: bool = True
          self.__status: enumerate = Status.ALIVE
          self.__imperium: "Imperium" = None

     def betray(self) -> None:
        self.__loyalty = False
        print(f"Primarch {self._name} betrays the Emperor")

     def change_status(self, status: enumerate) -> None:
        self.__status = status 

     def set_imperium(self, imperium: "Imperium") -> None:
        self.__imperium = imperium

     @property
     def name(self) -> str:
        return self._name