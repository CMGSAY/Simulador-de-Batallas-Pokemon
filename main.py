# Simulador de Batallas Pokémon
# Importamos el archivo pokedex.py que contine los datos de catálogo de Pokémon 
from batalla_pokemon import iniciar_batalla

def main():
    
    juego = True
    print('='*55)
    print('SIMULADOR DE BATALLAS POKEMON (POO)')
    print('='*55)


    while juego:
        opcion = int(input(('''
            Seleccione el Modo de juego: 
            1. Jugador vs Jugador
            2. Jugador vs Computadora
            3. Salir
            ''')))
        
        match opcion:
            case  1:
                print('Jugador vs jugador')
                iniciar_batalla(False)
            case 2:
                print('Jugador vs Computadora')
                iniciar_batalla(True)
            case 3:
                print('Saliendo del juego')
                break
            case _:
                print('pción inválida')
                


if __name__ == "__main__":
    main()