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
  
  def get_chapter_by_primarch(self,primarch:Primarch)->Chapter:
      for chapter in self.__chapters:
          if chapter.primarch== primarch:
              return chapter
      return None
         

class Chapter():

    def __init__(self, name:str,primarch: Primarch , planet:str) -> None:
        self.__name: str = name
        self.__primarch: Primarch = primarch
        #self.__planet: str = planet
        self.__Astartes: List[Astarte] = []
        self.__succesor_chapters: List[Chapter] = []
        

    def add_astarte(self, astarte: Astarte) -> None:
     try:
        if self.check_astartes() == 1000:
           print(f'Chapter {self.name} is full')

        if self.check_astartes() >= 1000:
            raise RuntimeError("There can only be 1000 Astartes per Chapter")
        self.__Astartes.append(astarte)
     except RuntimeError as e:
        print(f"{type(e).__name__}: {str(e)}")
        

        

    def check_astartes(self)->int:
        return len(self.__Astartes)

    def add_successor_chapter(self,chapter:Chapter)->None:
        self.__succesor_chapters.append(chapter)
        print(f'Added Successor Chapter {chapter.name} to Chapter {self.__name}')

    @property
    def name(self)->str:
        return self.__name
    
    @property
    def primarch(self)->Primarch:
        return self.__primarch
    
    @property
    def succcesor_chapters(self)->List[Chapter]:
        return self.__succesor_chapters