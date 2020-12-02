import json
import random
from Constantes import *
from modelos.Tipos import *


def crear_pokemon(nombre, nivel):
    pass


class Batalla:
    """
    Modelo de batalla.
    """

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.turno_actual = 0

    def finalizada(self):
        final = self.pokemon1.hp_actual <= 0 or self.pokemon2.hp_actual <= 0
        if final:
            self.print_win()
        return final

    def ejecutar_turno(self, turno):
        comando1 = turno.comando_1
        comando2 = turno.comando_2

        if SELECIONAR_ATAQUE in comando1.accion.keys():
            ataque1 = self.pokemon1.ataques[comando1.accion[SELECIONAR_ATAQUE]]

        if SELECIONAR_ATAQUE in comando2.accion.keys():
            ataque2 = self.pokemon2.ataques[comando2.accion[SELECIONAR_ATAQUE]]

        self.pokemon1.hp_actual -= self.calculo_de_daño(
            ataque1, self.pokemon2, self.pokemon1
        )
        self.pokemon2.hp_actual -= self.calculo_de_daño(
            ataque2, self.pokemon1, self.pokemon2
        )
        self.turno_actual += 1

    def calculo_de_daño(self, ataque, pokemon_defensor, pokemon_atacante):

        ocurrencia = ataque.ocurrencia
        if not random.randint(0, 99) < ocurrencia:
            print("Ataque fallo")
            return 0

        aux = 0.4 * pokemon_atacante.nivel + 2
        poder_ataque = 0.02 * aux * ataque.potencia
        stats_pokemon_atacante = pokemon_atacante.stats
        stats_pokemon_defensor = pokemon_defensor.stats

        if ataque.categoria == FISICO:
            valor = 2 + (
                poder_ataque
                * stats_pokemon_atacante[ATAQUE]
                / stats_pokemon_defensor[DEFENSA]
            )
        else:
            valor = 2 + (
                poder_ataque
                * stats_pokemon_atacante[ATAQUE_ESPECIAL]
                / stats_pokemon_defensor[DEFENSA_ESPECIAL]
            )
        mod = self.modificador(ataque, pokemon_defensor, pokemon_atacante)
        valor = mod * valor
        return round(valor)

    def modificador(self, ataque, pokemon_defensor, pokemon_atacante):
        # Calculo del daño por stab
        stab = 1
        if ataque.tipo in pokemon_atacante.tipos:
            stab = 1.5

        # Calculo del daño por tipo
        tipo1, tipo2 = pokemon_defensor.tipos
        efectividad_tipo1 = EFECTIVIDAD_DE_TIPOS[TIPOS.index(tipo1)][
            TIPOS.index(ataque.tipo)
        ]
        efectividad_tipo2 = 1
        if tipo2 is not None:
            efectividad_tipo2 = EFECTIVIDAD_DE_TIPOS[TIPOS.index(tipo2)][
                TIPOS.index(ataque.tipo)
            ]
        efectividad_tipo = efectividad_tipo1 * efectividad_tipo2

        # Calculo de los Criticos
        critico = 1
        if random.random() < 0.15:
            critico = 1.75

        valor = stab * efectividad_tipo * critico
        return valor

    def print_hp(self):
        print(
            f"{self.pokemon1.nombre}\
             tiene {self.pokemon1.hp_actual} puntos de vida"
        )
        print(
            f"{self.pokemon2.nombre}\
             tiene {self.pokemon2.hp_actual} puntos de vida"
        )

    def print_win(self):
        if self.pokemon1.hp_actual > 0 and self.pokemon2.hp_actual <= 0:
            print(
                f"El ganador es {self.pokemon1.nombre}\
                 en {self.turno_actual} turnos"
            )
        elif self.pokemon2.hp_actual > 0 and self.pokemon1.hp_actual <= 0:
            print(
                f"El ganador es {self.pokemon2.nombre}\
                 en {self.turno_actual} turnos"
            )
        else:
            print("Doble KO...")


class Turno:
    def __init__(self, comando_1, comando_2):
        self.comando_1 = comando_1
        self.comando_2 = comando_2


class Comando:
    def __init__(self, accion):
        self.accion = accion


def agregar_comando(pokemon):
    comando = None
    while not comando:
        print("Opciones de combate:")
        print("1) Atacar")
        print("2) Cambiar pokemon")
        try:
            comando_temporal = int(input(f"Que va a hacer {pokemon.nombre}: "))
        except Exception as error:
            pass

        if comando_temporal == 1:
            print("Ataques:")
            i = 0
            for ataque in pokemon.ataques:
                print(f"{i}) {ataque}")
                i += 1
            try:
                indice = int(input("Que ataque, deseas ocupar: "))
            except Exception as error:
                pass
            comando = Comando({SELECIONAR_ATAQUE: indice})
    return comando
