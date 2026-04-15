# Simulador de Batallas Pokémon
# Importamos el archivo pokedex.py que contine los datos de catálogo de Pokémon 
from pokedex import mostrar_catalogo_disponible



print('='*55)
print('SIMULADOR DE BATALLAS POKEMO (POO)')
print('='*55)

juego = True
while juego:
    opcion = int(input(('''
          Seleccione el Modo de juego: 
          1. Jugador vs Jugador
          2. Jugador vs Computadora
          3. Salir
          ''')))
    
    match opcion:
        case  1:
            print(' Jugador vs Jugador')
            # Imprimimos los pokémon disponibles en el catálogo
            print(mostrar_catalogo_disponible())
        case 2:
            print('Jugador vs Computadora')
            # Imprimimos los pokémon disponibles en el catálogo
            print(mostrar_catalogo_disponible())
        case 3:
            print('Saliendo del juego')
            break
        case _:
            print('[ValueError]')