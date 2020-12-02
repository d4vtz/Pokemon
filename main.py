import pickle
from modelos.Pokemon import *
from modelos.Naturalezas import *
from modelos.Tipos import *
from modelos.Batalla import *
from Constantes import *


pokemon_1 = Pokemon(PIKACHU, 85)
pokemon_2 = Pokemon(GYARADOS, 85)


print(pokemon_1.hp_actual)
print(pokemon_2.hp_actual)


batalla = Batalla(pokemon_1, pokemon_2)

while not batalla.finalizada():
    comando_1 = agregar_comando(pokemon_1)
    comando_2 = agregar_comando(pokemon_2)
    turno = Turno(comando_1, comando_2)
    batalla.ejecutar_turno(turno)
    batalla.print_hp()
