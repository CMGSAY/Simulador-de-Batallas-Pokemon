# importamos el archivo para crear la clase abtracta
from abc import ABC, abstractmethod
# Definimos la clase Pokemonses, que representará a cada Pokémon en el juego
class Pokemon(ABC):
    
    # Creamos el con el construcotr con Atributos de clase  
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.nombre = nombre
        self.hp_maximo = hp_maximo
        self.__hp_actual = hp_maximo
        self.energia_maxima = energia_maxima
        self.__energia_actual = energia_maxima
        self.defensa_activa = False
    
    
    # defenimos el metodo para mostar el hp actual
    @property
    def __hp_actual(self):
        return self.__hp_actual
    
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
            
    
    # defenimos el metodo para mostar la energia actual
    @property
    def __energia_actual(self):
        return self.__energia_actual
    
    @energia_actual.setter
    def energia_actual(self, energia_nueva):
        if energia_nueva < 0:
            self.energia_actual = 0

        elif energia_nueva > self.energia_maxima:
            self.energia_actual = self.energia_maxima

        else:
            self.energia_actual = energia_nueva

        
        #creacion del metodo abastracto 
        @abstractmethod
        def atacar(self):
            pass
        
        def defender(self):
            if self.energia_actual >= 5:
                self.energia_actual = self.energia_actual - 5
                print(f'{self.nombre} Se prepara para defender..')
            else:
                print(f'{self.nombre} No tiene energia suficiente para atacar.')
        
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
            
    

    