# batalla_pokemon.py

import random
from pokedex import CATALOGO_POKEMON, mostrar_catalogo

from pokemon_agua import PokemonAgua
from pokemon_fuego import PokemonFuego
from pokemon_planta import PokemonPlanta
from pokemon_electrico import PokemonElectrico


def instanciar_pokemon(datos):

    tipo = datos["tipo"]
    nombre = datos["nombre"]
    hp_max = datos["hp_maximo"]
    ep_max = datos["energia_maxima"]

    if tipo == "Agua":
        return PokemonAgua(nombre, hp_max, ep_max)

    elif tipo == "Fuego":
        return PokemonFuego(nombre, hp_max, ep_max)

    elif tipo == "Planta":
        return PokemonPlanta(nombre, hp_max, ep_max)

    elif tipo == "Electrico":
        return PokemonElectrico(nombre, hp_max, ep_max)


def elegir_pokemon(jugador):

    mostrar_catalogo()

    while True:

        try:

            opcion = int(input(f"Jugador {jugador} elija su Pokémon: "))

            if opcion in CATALOGO_POKEMON:

                datos = CATALOGO_POKEMON[opcion]
                pokemon = instanciar_pokemon(datos)

                print(f"{pokemon.nombre} elegido")
                return pokemon

        except ValueError:
            print("Entrada inválida")


def elegir_accion_pc():
    return random.choice([1, 2, 3])


def ejecutar_turno(pokemon, oponente, es_pc=False):

    print(f"\nTurno de {pokemon.nombre}")

    if es_pc:
        accion = elegir_accion_pc()

    else:
        print("1. Atacar")
        print("2. Defender")
        print("3. Descansar")

        accion = int(input("Opción: "))

    if accion == 1:
        pokemon.atacar(oponente)

    elif accion == 2:
        pokemon.defender()

    elif accion == 3:
        pokemon.descansar()


def batalla(p1, p2, modo_pc):

    turno = 1

    while p1.esta_vivo() and p2.esta_vivo():

        if turno % 2 != 0:
            ejecutar_turno(p1, p2)

        else:
            ejecutar_turno(p2, p1, modo_pc)

        turno += 1

    if p1.esta_vivo():
        print(f"{p1.nombre} gana")

    else:
        print(f"{p2.nombre} gana")


def iniciar_batalla(modo_pc):

    p1 = elegir_pokemon(1)

    if modo_pc:

        indice = random.choice(list(CATALOGO_POKEMON.keys()))
        datos = CATALOGO_POKEMON[indice]

        p2 = instanciar_pokemon(datos)

        print(f"La computadora eligió {p2.nombre}")

    else:
        p2 = elegir_pokemon(2)

    batalla(p1, p2, modo_pc)