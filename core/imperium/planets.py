from __future__ import annotations
from typing import List



class Segmentun:

    def __init__(self,name:str, location:str) -> None:
        self.__name: str = name
        self.__location: str = location
        self.__planets: List[Planet] = []
        pass

    def add_planet(self,planet:Planet)->None:
        self.__planets.append(planet)
        print(f"Added {planet.get_name()} to Segmentum {self.__name}")
    
    def get_planets(self)->List[Planet]:
        return self.__planets
class Planet:

    def __init__(self,planet_info: dict):
        self.__name = planet_info["planet_name"]
        self.__type_= planet_info["planet_type"]   
        chapter: "Chapter"  = None
        regiments: List["Regiment"] = []


    def get_name(self)->str:
        return self.__name
