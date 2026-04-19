from pokemon_clase_padre import Pokemon


class PokemonPlanta(Pokemon):

    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
        self.tipo = "Planta"


    def atacar(self, oponente):

        costo_ep = 15

        if self.energia_actual < costo_ep:
            print("Energía insuficiente para atacar.")
            return

        self.energia_actual -= costo_ep
        danio_base = 15


        from pokemon_agua import PokemonAgua
        from pokemon_fuego import PokemonFuego
        from pokemon_electrico import PokemonElectrico


        if isinstance(oponente, PokemonAgua):
            multiplicador = 2.0
            mensaje = "¡Es súper efectivo!"

        elif isinstance(oponente, (PokemonPlanta, PokemonFuego, PokemonElectrico)):
            multiplicador = 1.0
            mensaje = "Ataque normal."

        else:
            multiplicador = 1.0
            mensaje = "Ataque normal."


        danio_final = danio_base * multiplicador

        print(f"¡{self.nombre} usa ataque de Planta!")
        print(mensaje)

        oponente.recibir_danio(danio_final)