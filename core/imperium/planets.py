from __future__ import annotations
from typing import List


class Segmentum:

    def __init__(self,name:str, location:str) -> None:
        self.__name: str = name
        self.__location: str = location
        self.__planets: List[Planet] = []
        pass

    def add_planet(self,planet:Planet)->None:
         self.__planets.append(planet)
         print(f"Added planet {planet.get_name()} to Segmentum {self.__name}")
    
    def get_planets(self)->List[Planet]:
        return self.__planets
    
    @property
    def name(self)->str:
        return self.__name
class Planet:

    def __init__(self,planet_info: dict):
        self.__name = planet_info["planet_name"]
        self.__type_= planet_info["planet_type"]   
        self.__chapter: "Chapter"  = None
        self.__regiments: List["Regiment"] = []


    def get_name(self)->str:
        return self.__name
    
    def add_chapter(self,chapter:Chapter)->None:
        self.__chapter = chapter


    def add_regiment(self,regiment:"Regiment")->None:
        self.__regiments.append(regiment)

    def get_type(self)->str:
        return self.__type_
    
    def get_regiments(self)->List["Regiment"]:
        return self.__regiments
    
    def get_all_soldiers(self)->List["Soldier"]:
        soldiers = []
        for regiment in self.__regiments:
            soldiers.extend(regiment.get_soldiers())
        return soldiers
    
    @property
    def name(self)->str:
        return self.__name