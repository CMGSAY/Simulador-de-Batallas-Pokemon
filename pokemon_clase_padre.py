# importamos el archivo para crear la clase abtracta
from abc import ABC, abstractmethod
# Definimos la clase Pokemonses, que representará a cada Pokémon en el juego
class Pokemon(ABC):
    
    # Atributos de clase  
    def __init__(self,tipo, nombre, hp_maximo, energia_maxima):
        self.tipo = tipo
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
    
    @hp_actual.setter
    def hp_actual(self, hp_nuevo):
        if hp_nuevo <= 0:
            self.hp_actual = 0
            print(f'{self.nombre} Se desmayo, perdio la batalla, [Salud Actual: ]{self.hp_actual}/{self.hp_maximo}.')
        elif hp_nuevo > self.hp_maximo:
            self.hp_actual = self.hp_maximo
            print(f'{self.nombre} Salud al maximo, [Salud Actual: ]{self.hp_actual}/{self.hp_maximo}.')
        else:
            self.hp_actual = hp_nuevo
            print(f'{self.nombre} [Salud Actual: ]{self.hp_actual}/{self.hp_maximo}. ')
            
    
    # defenimos el metodo para mostar la energia actual
    @property
    def __energia_actual(self):
        return self.__energia_actual
    
    @energia_actual.setter
    def energia_actual(self, energia_nueva):
        if energia_nueva <= 0:
            self.energia_actual = 0
            print(f'{self.nombre} No tiene energia para atacar [Energia: ]{self.energia_actual}/{self.energia_maxima}')
        elif energia_nueva > self.energia_maxima:
            self.energia_actual = self.energia_maxima
            print(f'{self.nombre} Energia actual para atacar [Energia: ]{self.energia_actual}/{self.energia_maxima}')
        else:
            self.energia_actual = energia_nueva
            print(f'{self.nombre} Energia actual para atacar [Energia: ]{self.energia_actual}/{self.energia_maxima}')
            
            
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
            pass
                 
        def recibir_daño(self):
            pass
    

    