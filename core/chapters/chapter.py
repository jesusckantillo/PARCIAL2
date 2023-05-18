from future import __annotations__
from typing import List
from utils.person import Primarch, Astarte


class AdeptusArtartes():
  def __init__(self):
   self.__chapters: List[Chapter] = []



class Chapter():

    def __init__(self, name:str,primarch: Primarch , planet:str) -> None:
        self.__name: str = name
        self.__primarch: Primarch = primarch
        #self.__planet: str = planet
        self.__Astartes: List[Astarte] = []
        self.__succesor_chapters: List[Chapter] = []
        

        pass
pass
