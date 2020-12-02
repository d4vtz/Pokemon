import json
import requests
from bs4 import BeautifulSoup
from Constantes import *


def normalizar(string):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        string = string.replace(a, b).replace(a.upper(), b.upper())
    return string


def stats_base_db():
    url = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/buscar"
    pagina = requests.get(url, timeout=5)
    contenido = BeautifulSoup(pagina.content, "html.parser")

    pokemon_db = contenido.find_all("tr", class_="bazul")[:151]
    stats_db = []
    for fila in pokemon_db:
        stats = fila.find_all("td")[3:9]
        stats_base = []
        for i in range(len(stats)):
            hp = int(stats[0].text)
            ataque = int(stats[1].text)
            defensa = int(stats[2].text)
            ataque_especial = int(stats[4].text)
            defensa_especial = int(stats[5].text)
            velocidad = int(stats[3].text)
            stats_base = [
                hp,
                ataque,
                defensa,
                ataque_especial,
                defensa_especial,
                velocidad,
            ]
        stats_db.append(stats_base)
    return stats_db


url = "https://www.wikidex.net/wiki/Lista_de_Pok%C3%A9mon_seg%C3%BAn_la_Pok%C3%A9dex_de_Kanto"
pagina = requests.get(url, timeout=5)
contenido = BeautifulSoup(pagina.content, "html.parser")

pokemon_db = contenido.find_all("table", class_="tabpokemon")
pokemon_filas = pokemon_db[0].find_all("tr")


POKEDEX = {}

stats = stats_base_db()
i = 0
for fila in pokemon_filas[1:]:
    numero = int(fila.find_all("td")[1].text[:-1])
    nombre = normalizar(fila.find_all("td")[3].text[:-1])
    tipos_html = fila.find_all("td")[4:]
    tipos = []
    for elemento in tipos_html:
        a = elemento.find_all("a")
        tipo = normalizar(str(a).split()[3][:-6].capitalize())
        tipos.append(tipo)
    if len(tipos) == 1:
        tipos.append(None)

    POKEDEX[nombre] = {
        "ID": numero,
        "TIPOS": tipos,
        "STATS": {
            HP: stats[i][0],
            ATAQUE: stats[i][1],
            DEFENSA: stats[i][2],
            ATAQUE_ESPECIAL: stats[i][3],
            DEFENSA_ESPECIAL: stats[i][4],
            VELOCIDAD: stats[i][5],
        },
    }
    i += 1

with open(DB_POKEDEX, "w") as db:
    json.dump(POKEDEX, db)
