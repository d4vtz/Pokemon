import json
import requests
import pickle
from bs4 import BeautifulSoup
from Constantes import *
from modelos.Ataques import *
from modelos.Pokemon import Ataque


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


"""
url = "https://www.pokexperto.net/index2.php?seccion=general/ataques1"
pagina = requests.get(url, timeout=5)
contenido = BeautifulSoup(pagina.content, "html.parser")

ataques_db = contenido.find_all("tr")
ATAQUES = {}
COMENTARIOS = []
i = 0
for fila in ataques_db[9:-7]:
    if i % 2 == 0:
        numero = int(fila.find("th").text)
        datos = fila.find_all("td")
        nombre = str(datos[0]).split(">")[1].split("<")[0]
        tipo = str(datos[1]).split('"')[3]
        categoria = str(datos[2]).split('"')[3]
        pp = int(datos[3].text)
        efectividad = datos[4].text
        poder = datos[5].text
        ATAQUES[nombre] = {
            "ID": numero,
            "TIPO": tipo,
            "CATEGORIA": categoria,
            "EFECTIVIDAD": efectividad,
            "PODER": poder,
            "PP": pp,
        }
    else:
        comentario = fila.find("td").text
        COMENTARIOS.append(comentario)
    i += 1
ATAQUES["COMENTARIOS"] = COMENTARIOS

with open(DB_ATAQUES, "w") as file:
    json.dump(ATAQUES, file)
"""


def crear_ataques():
    with open(DB_ATAQUES, "r") as file:
        data = json.load(file)
    ATAQUES_DB = {}
    i = 0
    for ataque in ATAQUES:
        datos = data[ataque]
        ataque_obj = Ataque(
            ataque,
            datos["ID"],
            datos["TIPO"],
            datos["CATEGORIA"],
            datos["PODER"],
            datos["EFECTIVIDAD"],
            datos["PP"],
            data["COMENTARIOS"][i],
        )
        ATAQUES_DB[ataque] = ataque_obj
        i += 1

    return ATAQUES_DB


with open(ATAQUES_OBJ, "wb") as file:
    pickle.dump(crear_ataques(), file)
