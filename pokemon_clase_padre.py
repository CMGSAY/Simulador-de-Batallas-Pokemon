# Importamos el archivo pokedex.py que contine los datos de catálogo de Pokémon
from pokedex import CATALOGO_POKEMON
# Definimos la clase Pokemonses, que representará a cada Pokémon en el juego
class Pokemon:
    # Atributos de clase  
    def __init__(self,tipo, nombre, hp_maximo, energia_maxima):
        self.tipo = tipo
        self.nombre = nombre
        self.hp_maximo = hp_maximo
        self.__hp_actual = hp_maximo
        self.energia_maxima = energia_maxima
        self.__energia_actual = energia_maxima
    
    # defenimos el metodo para mostar el hp actual
    @property
    def __hp_actual(self):
        return self.__hp_actual9
    
    # defenimos el metodo para mostar la energia actual
    @property
    def __energia_actual(self):
        return self.__energia_actual
    

    