from __future__ import annotations
from typing import List
from utils.person import Primarch, Astarte


class AdeptusAstartes():
  def __init__(self)->None:
   self.__chapters: List[Chapter] = []


  def add_chapter(self,chapter:Chapter)->None:
      self.__chapters.append(chapter)

  def get_chapter(self,index:int)->Chapter:
        return self.__chapters[index]
         

class Chapter():

    def __init__(self, name:str,primarch: Primarch , planet:str) -> None:
        self.__name: str = name
        self.__primarch: Primarch = primarch
        #self.__planet: str = planet
        self.__Astartes: List[Astarte] = []
        self.__succesor_chapters: List[Chapter] = []
        

    def add_astarte(self,astarte:Astarte)->None:
        self.__Astartes.append(astarte)

    def add_successor_chapter(self,chapter:Chapter)->None:
        self.__succesor_chapters.append(chapter)