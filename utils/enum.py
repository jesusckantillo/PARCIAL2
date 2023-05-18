from enum import Enum

class Status(Enum):

    ALIVE = 'Alive'
    DEAD = 'Dead'
    UNKNOW = 'Unknow'

class PlanetTyped(Enum):

    AGRI = 'Agri'
    CIVILISED = 'Civilised'
    DAEMON = 'Daemon'
    DEAD = 'Dead'
    DEATH = 'Death'
    FERAL = 'Feral'
    FEUDAL = 'Feudal'
    FORGE = 'Forge'
    FRONTIER = 'Frontier'
    HIVE = 'Hive'