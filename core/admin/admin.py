from  __future__  import annotations
from typing import List
from person.person import Primarch
class Administratum():

    def __init__(self) -> None:
        self.__bureaucrats: List[Bureaucrat] = []
        self.__planet_registry: List[int] = []

    def add_bureaucrat(self, bureaucrat: Bureaucrat) -> None:
        self.__bureaucrats.append(bureaucrat)

    def get_burocrat(self, index: int) -> Bureaucrat:
        return self.__bureaucrats[index]