import json
import random
import pickle
from Constantes import *
from modelos.Naturalezas import *
from modelos.Ataques import *


class Pokemon:
    """
    Modelo de pokemon.
    """

    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

        self.ataques = self.__seleccionar_ataques()

        with open(DB_POKEDEX, "r") as file:
            pokedex = json.load(file)
        self.tipos = pokedex[nombre]["TIPOS"]

        self.estado = 0
        self.naturaleza = self.__definir_naturaleza()
        self.ev = self.__calcular_ev()
        self.iv = self.__calcular_iv()
        self.stats_base = pokedex[nombre]["STATS"]
        self.stats = self.__calcular_stats()
        self.hp_actual = self.stats[HP]

    def __seleccionar_ataques(self):
        with open(ATAQUES_OBJ, "rb") as file:
            ataques = pickle.load(file)
        mis_ataques = []
        for i in range(6):
            mis_ataques.append(random.choice(list(ataques.values())))
        return mis_ataques

    def __definir_naturaleza(self):
        return random.choice(list(NATURALEZA.keys()))

    def __calcular_ev(self):
        while True:
            ev = {}
            for stat in STATS:
                ev[stat] = random.randint(1, 255)
            suma = sum(ev.values())
            if suma < 510:
                break
        return ev

    def __calcular_iv(self):
        iv = {}
        for stat in STATS:
            iv[stat] = random.randint(0, 31)
        return iv

    def __calcular_stats(self):
        stats = {}
        for stat in STATS:
            if stat == HP:
                stats[stat] = self.__calcular_hp()
            else:
                stats[stat] = self.__calcular_stats_estandar(stat)
        return stats

    def __calcular_hp(self):
        valor = 2 * self.stats_base[HP] + self.iv[HP] + 0.25 * self.ev[HP]
        valor = (self.nivel / 100) * valor
        valor = valor + self.nivel + 10
        return round(valor)

    def __calcular_stats_estandar(self, stat):
        val = 2 * self.stats_base[stat] + self.iv[stat] + 0.25 * self.ev[stat]
        valor = (self.nivel / 100) * val
        valor = (valor + 5) * NATURALEZA[self.naturaleza][stat]
        return round(valor)


class Ataque:
    """
    Modelo de Ataque.
    """

    def __init__(
        self, nombre, id, tipo, categoria, potencia, ocurrent, pts, comentario
    ):
        self.nombre = nombre
        self.id = id
        self.tipo = tipo
        self.categoria = categoria
        self.potencia = potencia
        self.ocurrencia = ocurrent
        self.puntos = pts
        self.comentario = comentario

    def __str__(self):
        return self.nombre
