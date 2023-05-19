from __future__ import annotations
from utils.person import Soldier
from typing import List


class AstraMilitarum():
    def __init__(self) -> None:
     self.__regiments: List[Regiment] = []


    def get_regiment(self, index: int) -> Regiment:
        return self.__regiments[index]
    
    def add_regiment(self, regiment: Regiment) -> None:
        self.__regiments.append(regiment)

class Regiment():
   def __init__(self, name: str, planet:str) -> None:
         self.__name: str = name
         self.__planet: str = planet
         self.__soldiers: List[Soldier] = []

   def add_soldier(self,soldier:Soldier)->None:
        self.soldiers.append(soldier)

   @property
   def name(self)->str:
        return self.__name
   
   @property
   def soldiers(self)->List[Soldier]:
        return self.soldiers
    