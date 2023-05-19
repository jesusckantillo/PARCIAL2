from __future__ import annotations
from typing import List, Optional
from collections import Counter

from core.imperium.planets import Planet, Segmentum
from utils.exceptions.exceptions import SingletonError
from utils.person import Primarch, Bureaucrat
from core.admin.militarum import AstraMilitarum, Regiment
from core.chapters.chapter import Chapter, AdeptusAstartes
from core.admin.admin import Administratum


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
        self.__segmentums: Segmentum = []
        self.__planet: Planet = Planet(planet_info)

        Imperium.__INSTANCE = self

    @classmethod
    def get_instance(cls):
         return cls.__INSTANCE
    
    def set_emperor(self, emperor: "Emperor") -> None:
        self.__emperor = emperor


    def add_primarch(self,primarch: Primarch)->None:
        try:
            if len(self.__primarchs)>=20:
                raise RuntimeError ("There can only be 20 Primarchs")
            else:
             self.__primarchs.append(primarch)
             if type(primarch) is Primarch:
                 name = primarch.name
             else:
                 name = "*****"
             print(f'The Emperor created Primarch {name}')
        except RuntimeError as e:
            print(f"{type(e).__name__}: {str(e)}")

    def add_segmentum(self,planet_info: dict)->None:
        segmentum = Segmentum(planet_info["segmentum_name"], planet_info["segmentum_location"])
        self.__segmentums.append(segmentum)


    def add_bureaucrat(self, bureaucrat:Bureaucrat)->None:
        self.__administratum.add_bureaucrat(bureaucrat)
        print(f'{bureaucrat.name} {bureaucrat.id_string} started to work at Imperium')

    def get_bureaucrat(self,index:int)->Bureaucrat:
        return self.__administratum.get_bureaucrat(index)

    def register_planet(self, bureaucrat:Bureaucrat, planet_info:dict)->None:
        planet = Planet(planet_info)
        bureaucrat.set_planet(planet)
     
    def get_chapter(self, index:int)->Chapter:
        try:
            return self.__adeptus_astartes.get_chapter(index)
        except RuntimeError as e:
            print(f"{type(e).__name__}: {str(e)}")

    def find_planet(self, name:str)->Optional[Planet]:
        for segmentum in self.__segmentums:
            for planet in segmentum.get_planets():
                if planet.get_name()== name:
                    return planet
        return None
    
    def add_chapter(self,name:str, primarch: Primarch, planetstr: str)->None:
        self.__adeptus_astartes.add_chapter(Chapter(name, primarch,self.find_planet(planetstr)))
        print(f'Created chapter {name} of Adeptus Astartes')

    def add_segmentum(self, segmentum: Segmentum)->None:
        self.__segmentums.append(segmentum)
        print(f'Added Segmentum {segmentum.name} to the Imperium')
        pass

    def add_regiment(self, name:str, name_planet:str)->None:
        find_planet = self.find_planet(name_planet)
        self.__astra_militarun.add_regiment(Regiment(name,find_planet))
        planet = self.find_planet(name_planet)
        planet.add_regiment(Regiment(name,planet))
        print(f'Created Regiment {name} of Astra Militarum')

    def get_regiment(self, index:int)->Regiment:
        return self.__astra_militarun.get_regiment(index)
    
    def register_planet(self, burecraut: Bureaucrat, planet_info: dict)->None:
         index = self.__administratum.get_bureaucrat_index(burecraut)
         try:
          if self.find_planet(planet_info["planet_name"]) == None:
            segmetun_instance = Segmentum(planet_info["segmentum_name"], planet_info["segmentum_location"]) 
            planet_instance = Planet(planet_info)
            self.add_planet_segmentun(planet_instance, segmetun_instance)
            self.__segmentums.append(segmetun_instance)
            self.__administratum.modify_registers(index)    
          else:
            raise RuntimeError("This planet already exists")
         except RuntimeError as e:
            print(f"{type(e).__name__}: {str(e)}")
            
    def bureaucrat_max_registry(self)->List[Bureaucratm, int]:
        return self.__administratum.max_registers()

    def find_segmentum(self, name:str)->Optional[Segmentun]:
        for segmentum in self.__segmentums:
            if segmentum.name == name:
                return segmentum
        return None
            
    def add_planet_segmentun(self, planet: Planet, segmentum: Segmentum)->None:
        try:
         if self.find_planet(planet.name) == None:
            segmentum.add_planet(planet)
         else:
            raise RuntimeError("This planet already exists")
        except RuntimeError as e:
            print(f"{type(e).__name__}: {str(e)}")
            


    def planet_type_quantity(self)->None:
      planet_counts = Counter()
      for segmentum in self.__segmentums:
        for planet in segmentum.get_planets():
            planet_type = planet.get_type()
            planet_counts[planet_type.value] += 1
        dictio = dict(planet_counts)
      print("---------- Planet Type ----------")
      for planet, quantity in sorted(dictio.items()):
        print("- {} Planet Quantity = {}".format(planet, quantity))
      print("")
   
    def get_chapter_by_primarch(self, primarch: Primarch)->Chapter:
        return self.__adeptus_astartes.get_chapter_by_primarch(primarch)

    def show_primarchs_summary(self)->None:
        NUMBERS = [
        "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
        "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"
         ]
        print("---------- Primarchs Summary ----------")
        for i in range(20):
          print(f"- Primarch {NUMBERS[i]}")
          if self.__primarchs[i] is not None:
            self.__primarchs[i].show_summary()
            for chapter in self.get_chapter_by_primarch(self.__primarchs[i]).succcesor_chapters:
                print(f"        -{chapter.name}")
          else:
            print("  - Purged from Imperial Registry")
          print("")

    def get_regiments_primarch_info(self, name:str)->int:
        soldiers = 0
        regi_amount =0
        for regiment in self.__astra_militarun.regiments:
            if regiment.planet.name == name:
                regi_amount += 1
                soldiers += len(regiment.soldiers)
        return [regi_amount,soldiers]
                


    @property
    def name(self)->str:
        return self.__name

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
        segmentum = Segmentum(planet_info["segmentum_name"], planet_info["segmentum_location"])
        planet = Planet(planet_info)
        segmentum.add_planet(planet)
        print(f'The Emperor created {name} at planet {planet_info["planet_name"]}')
        self.__imperiun = imperium_instance
        self.__imperiun.add_segmentum(segmentum)     
        imperium_instance.set_emperor(self)


    def create_primarch(self, name: str=None, alias:str=None,planet_info:dict=None):
        if name is None and alias is None and planet_info is None:
         self.__imperiun.add_primarch(None)
        else:
         primarch = Primarch(name, alias, planet_info)
         primarch.set_imperium(self.__imperiun)
         if self.__imperiun.find_segmentum(planet_info["segmentum_name"]) == None:
                  segmentum_instance = Segmentum(planet_info["segmentum_name"], planet_info["segmentum_location"])
                  planet_instance = Planet(planet_info)
                  self.__imperiun.add_segmentum(segmentum_instance)
                  self.__imperiun.add_planet_segmentun(planet_instance, segmentum_instance)  
                  primarch.set_imperium(self.__imperiun)
                  self.__imperiun.add_primarch(primarch)     
         else:
             segmentun_instance = self.__imperiun.find_segmentum(planet_info["segmentum_name"])
             planet_instance = Planet(planet_info)
             self.__imperiun.add_planet_segmentun(planet_instance, segmentun_instance)
             primarch.set_imperium(self.__imperiun)
             self.__imperiun.add_primarch(primarch)

    
