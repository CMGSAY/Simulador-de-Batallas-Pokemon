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
    def hp_actual(self):
        return self.__hp_actual
    
    # defenimos el metodo para mostar la energia actual
    @property
    def ep_actual(self):
        return self.__ep_actual
    

# Creamos clases hijas para cada tipo de Pokemon
class PokemonAgua(Pokemon):
    pass

class PokemonFuego(Pokemon):
    pass

class PokemonPlanta(Pokemon):
    pass

class PokemonElectrico(Pokemon):
    pass


    