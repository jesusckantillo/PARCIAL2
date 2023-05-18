from future import __annotations__
from typing import List
from utils.person import Primarch, Astarte


class AdeptusArtartes():
  def __init__(self)->None:
   self.__chapters: List[Chapter] = []


  def add_chapter(self,chapter:Chapter)->None:
      self.__chapters.append(chapter)


class Chapter():

    def __init__(self, name:str,primarch: Primarch , planet:str) -> None:
        self.__name: str = name
        self.__primarch: Primarch = primarch
        #self.__planet: str = planet
        self.__Astartes: List[Astarte] = []
        self.__succesor_chapters: List[Chapter] = []
        

    def add_astarte(self,astarte:Astarte)->None:
        self.__Astartes.append(astarte)

    def add_succesor_chapter(self,chapter:Chapter)->None:
        self.__succesor_chapters.append(chapter)