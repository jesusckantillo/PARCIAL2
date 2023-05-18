from __future__ import annotations
from typing import List



class Segmentun:

    def __init__(self,name:str, location:str) -> None:
        self.__name: str = name
        self.__location: str = location
        self.__planets: List[Planet] = []
        pass



class Planet:

    def __init__(self,planet_info: dict):
        self.__name = planet_info["planet_name"]
        self.__type_= planet_info["planet_type"]   
        chapter: "Chapter"  = None
        regiments: List["Regiment"] = []

