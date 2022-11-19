from abc import ABC, abstractmethod



class Enemy1(ABC):

    @abstractmethod
    def spawn_enemy(self):
        """Crea el enemigo"""

class Enemy2(ABC):

    @abstractmethod
    def spawn_enemy(self):
        """Crea el enemigo"""


class Difficult_Enemy1(ABC):

    @abstractmethod
    def spawn_enemy(self):
        """Crea el enemigo dificil"""
        
class Difficult_Enemy2(ABC):

    @abstractmethod
    def spawn_enemy(self):
        """Crea el enemigo dificil"""




class Enemy_Factory(ABC):

    def get_enemy1(self) -> Enemy1:
        pass

    def get_enemy2(self) -> Enemy2:
        pass


class Difficult_Enemy_Factory(Enemy_Factory):

    def get_enemy1(self) -> Enemy1:
        return Difficult_Enemy1()

    def get_enemy2(self) -> Enemy2:
        return Difficult_Enemy2()
