# importamos el archivo para crear la clase abstracta
from abc import ABC, abstractmethod


# Definimos la clase Pokemon
class Pokemon(ABC):

    # Constructor
    def __init__(self, nombre, hp_maximo, energia_maxima):

        self.nombre = nombre
        self.hp_maximo = hp_maximo
        self.__hp_actual = hp_maximo

        self.energia_maxima = energia_maxima
        self.__energia_actual = energia_maxima

        self.defensa_activa = False


    @property
    def hp_actual(self):
        return self.__hp_actual


    @hp_actual.setter
    def hp_actual(self, nuevo_hp):

        if nuevo_hp < 0:
            self.__hp_actual = 0

        elif nuevo_hp > self.hp_maximo:
            self.__hp_actual = self.hp_maximo

        else:
            self.__hp_actual = nuevo_hp



    @property
    def energia_actual(self):
        return self.__energia_actual


    @energia_actual.setter
    def energia_actual(self, energia_nueva):

        if energia_nueva < 0:
            self.__energia_actual = 0

        elif energia_nueva > self.energia_maxima:
            self.__energia_actual = self.energia_maxima

        else:
            self.__energia_actual = energia_nueva


    @abstractmethod
    def atacar(self, oponente):
        pass


    def defender(self):

        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.defensa_activa = True

            print(f"{self.nombre} se prepara para defenderse.")

        else:
            print(f"{self.nombre} no tiene energía suficiente.")


    def descansar(self):

        cantidad = 20
        self.energia_actual += cantidad

        print(f"{self.nombre} descansa y recupera {cantidad} EP.")


    def recibir_danio(self, danio_base):

        if self.defensa_activa:
            danio_base = danio_base // 2
            self.defensa_activa = False

        self.hp_actual -= danio_base

        print(f"{self.nombre} recibe {danio_base} puntos de daño.")


    def esta_vivo(self):
        return self.hp_actual > 0