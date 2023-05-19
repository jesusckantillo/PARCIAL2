from  __future__  import annotations
from typing import List
class Administratum():

    def __init__(self) -> None:
        self.__bureaucrats: List[Bureaucrat] = []
        self.__planet_registry: List[int] = []

    def add_bureaucrat(self, bureaucrat: Bureaucrat) -> None:
        self.__bureaucrats.append(bureaucrat)
        self.__planet_registry.append(0)

    
    def modify_registers(self, index:int)->None:
        self.__planet_registry[index] +=1
    
    def get_bureaucrat(self, index: int) -> Bureaucrat:
        return self.__bureaucrats[index]

    def get_bureaucrat_index(self, bureaucrat: Bureaucrat) -> int:
        return self.__bureaucrats.index(bureaucrat)