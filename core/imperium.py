from __future__ import annotations
from typing import List
from person.primarch import Primarch
from core.planets import Planet
from core.admin import Administratum

class Imperium:
    def __init__(self, name: str, planet_info: dict):
        self.__emperor: "Emperor" = None
        self.__name: str = name
        self.__primarchs: Primarch = []
        self.__adeptus_astartes: AdeptusAstartes = []
        self.__administratum: Administratum = Administratum()
        self.__segmentums: Segmentum = []
        self.__planet: Planet = Planet(planet_info)

    def set_planet(self, planet_info: dict) -> None:
        self.__planet = Planet(planet_info)

    def add_primarch(self,primarch: Primarch)->None:
        self.__primarchs.append(primarch)

    def add_segmentun(self,planet_info: dict)->None:
        segmentun = Segmentun(planet_info["segmentum_name"], planet_info["segmentum_location"])
        self.__segmentums.append(segmentun)


    def add_bureaucreat(self, bureaucrat:Bureaucrat )->None:
        self.__

    
    @property
    def primarchs(self)->List[Primarch]:
        return self.__primarchs
    

class Emperor:
    def __init__(self)->None:
        self.__imperiun: "Imperium" =  None


    def create_imperium(self, name: str, planet_info: dict) -> Imperium:
        Imperium = Imperium(name, planet_info)
        self.__imperiun = Imperium
        Imperium.set_emperor(self)

    def create_primarch(self, name: str, alias:str,planet_info:dict):
        primarch = Primarch(name, alias, planet_info)
        self.__imperiun.add_primarch(primarch)
       


    