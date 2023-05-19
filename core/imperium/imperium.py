from __future__ import annotations
from __future__ import annotations
from typing import List


#from utils.person import Primarch, Bureaucrat
from core.imperium.planets import Planet, Segmentun
from utils.exceptions.exceptions import SingletonError
from utils.person import Primarch
from core.admin.militarum import AstraMilitarum, Regiment
from core.chapters.chapter import Chapter, AdeptusAstartes
from core.admin.admin import Administratum
#from admin.militarum import AstraMilitarum, Regiment

class Imperium:

    __INSTANCE = None

    def __init__(self, name: str, planet_info: dict):
        if not Imperium.__INSTANCE is None:
            raise SingletonError('')
        self.__emperor: "Emperor" = None
        self.__name: str = name
        self.__primarchs: "Primarch" = []
        self.__adeptus_astartes: "AdeptusAstartes" = AdeptusAstartes()
        self.__administratum: "Administratum" = Administratum()
        self.__astra_militarun: "AstraMilitarum" = AstraMilitarum()
        self.__segmentums: Segmentun = []
        self.__planet: Planet = Planet(planet_info)

        Imperium.__INSTANCE = self

    @classmethod
    def get_instance(cls):
         return cls.__INSTANCE
    
    def set_emperor(self, emperor: "Emperor") -> None:
        self.__emperor = emperor


    def set_planet(self, planet_info: dict) -> None:
        self.__planet = Planet(planet_info)

    def add_primarch(self,primarch: Primarch)->None:
        self.__primarchs.append(primarch)

    def add_segmentun(self,planet_info: dict)->None:
        segmentun = Segmentun(planet_info["segmentum_name"], planet_info["segmentum_location"])
        self.__segmentums.append(segmentun)


    def add_bureaucreat(self, bureaucrat:Bureaucrat )->None:
        self.__administratum.add_bureaucrat(bureaucrat)

    def get_bureaucrat(self,index:int)->Bureaucrat:
        return self.__administratum.get_bureaucrat(index)

    
    #Bureaucrat's index -> Planet's index
    def register_planet(self, bureaucrat:Bureaucrat, planet_info:dict)->None:
        planet = Planet(planet_info)
        bureaucrat.set_planet(planet)
    

    def get_chapter(self, index:int)->Chapter:
        return self.__adeptus_astartes.get_chapter(index)


    def find_planet(self, name:str)->Planet:
        for segmentun in self.__segmentums:
            for planet in segmentun.get_planets():
                if planet.get_name()== name:
                    return planet

    #Rercuerda que chapter es reflexiva
    def add_chapter(self,name:str, primarch: Primarch, planetstr: str)->None:
        self.__adeptus_astartes.add_chapter(Chapter(name, primarch,self.find_planet(planetstr)))

    
    def add_bureaucrat(self, bureaucrat: Bureaucrat)->None:
        self.__administratum.add_bureaucrat(bureaucrat)


    def add_segmentun(self, segmentun: Segmentun)->None:
        self.__segmentums.append(segmentun)
        pass

    def add_regiment(self, name:str, name_planet:str)->None:
        self.__astra_militarun.add_regiment(Regiment(name,self.find_planet(name_planet)))

    def get_regiment(self, index:int)->Regiment:
        return self.__astra_militarun.get_regiment(index)
    
    def add_segmentun(self, segmentun: Segmentun)->None:
        self.__segmentums.append(segmentun)



    def register_planet(self, burecraut: Bureaucrat, planet_info: dict)->None:
         index = self.__administratum.get_bureaucrat_index(burecraut)
         if self.find_planet(planet_info["planet_name"]) == None:
            self.__administratum.modify_registers(index)    

    @property
    def primarchs(self)->List[Primarch]:
        return self.__primarchs
    

class Emperor:
    __INSTANCE = None

    def __init__(self) -> None:
        if Emperor.__INSTANCE is not None:
            raise SingletonError("There can only be one Emperor of Mankind")
        Emperor.__INSTANCE = self
        self.__imperiun: Imperium = None
        print("The Emperor of Mankind has arisen")


    @classmethod
    def get_instance(cls):
         return cls.__INSTANCE
    

    def create_imperium(self, name: str, planet_info: dict):
        imperium_instance = Imperium(name, planet_info)
        segmentun = Segmentun(planet_info["segmentum_name"], planet_info["segmentum_location"])
        planet = Planet(planet_info)
        segmentun.add_planet(planet)
        self.__imperiun = imperium_instance
        imperium_instance.set_emperor(self)

    #Sobrecarga de metodos 
    def create_primarch(self, name: str=None, alias:str=None,planet_info:dict=None):
        if name is None and alias is None and planet_info is None:
         self.__imperiun.add_primarch(None)
        else:
         primarch = Primarch(name, alias, planet_info)
         segmentun = Segmentun(planet_info["segmentum_name"], planet_info["segmentum_location"])
         planet = Planet(planet_info)
         primarch.set_imperium(self.__imperiun)
         self.__imperiun.add_primarch(primarch)
         if self.__imperiun.find_planet(planet) == None:
            segmentun.add_planet(planet)
            self.__imperiun.add_segmentun(segmentun)
         else:
            print("Ya existe")