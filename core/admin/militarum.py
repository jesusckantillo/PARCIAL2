from __future__ import annotations
from typing import List
from utils.person import Soldier

class AstraMilitarum():
    def __init__(self) -> None:
     self.__regiments: List[Regiment] = []


    def get_regiment(self, index: int) -> Regiment:
        return self.__regiments[index]

class Regiment():
   def __init__(self, name: str, planet:str) -> None:
         self.__name: str = name
         self.__planet: str = planet
         self.soldiers: List[Soldier] = []

   def add_soldier(self,soldier:Soldier)->None:
        self.soldiers.append(soldier)
    