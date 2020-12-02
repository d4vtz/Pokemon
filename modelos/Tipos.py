# TIPOS
NORMAL = "Normal"
LUCHA = "Lucha"
VOLADOR = "Volador"
VENENO = "Veneno"
TIERRA = "Tierra"
ROCA = "Roca"
BICHO = "Bicho"
FANTASMA = "Fantasma"
ACERO = "Acero"
FUEGO = "Fuego"
AGUA = "Agua"
PLANTA = "Planta"
ELECTRICO = "Electrico"
PSIQUICO = "Psiquico"
HIELO = "Hielo"
DRAGON = "Dragon"
SINIESTRO = "Siniestro"
HADA = "Hada"


TIPOS = [
    NORMAL,
    LUCHA,
    VOLADOR,
    VENENO,
    TIERRA,
    ROCA,
    BICHO,
    FANTASMA,
    ACERO,
    FUEGO,
    AGUA,
    PLANTA,
    ELECTRICO,
    PSIQUICO,
    HIELO,
    DRAGON,
    SINIESTRO,
    HADA,
]

EFECTIVIDAD_DE_TIPOS = [
    # NORMAL
    [
        1.0,  # NORMAL
        1.0,  # LUCHA
        1.0,  # VOLADOR
        1.0,  # VENENO
        1.0,  # TIERRA
        0.5,  # ROCA
        1.0,  # BICHO
        0.0,  # FANTASMA
        0.5,  # ACERO
        1.0,  # FUEGO
        1.0,  # AGUA
        1.0,  # PLANTA
        1.0,  # ELECTRICO
        1.0,  # PSIQUICO
        1.0,  # HIELO
        1.0,  # DRAGON
        1.0,  # SINIESTRO
        1.0,  # HADA
    ],
    # LUCHA
    [
        2.0,  # NORMAL
        1.0,  # LUCHA
        0.5,  # VOLADOR
        0.5,  # VENENO
        1.0,  # TIERRA
        2.0,  # ROCA
        0.5,  # BICHO
        0.0,  # FANTASMA
        2.0,  # ACERO
        1.0,  # FUEGO
        1.0,  # AGUA
        1.0,  # PLANTA
        1.0,  # ELECTRICO
        0.5,  # PSIQUICO
        2.0,  # HIELO
        1.0,  # DRAGON
        2.0,  # SINIESTRO
        0.5,  # HADA
    ],
    # VOLADOR
    [
        1.0,  # NORMAL
        2.0,  # LUCHA
        1.0,  # VOLADOR
        1.0,  # VENENO
        1.0,  # TIERRA
        0.5,  # ROCA
        2.0,  # BICHO
        1.0,  # FANTASMA
        0.5,  # ACERO
        1.0,  # FUEGO
        1.0,  # AGUA
        2.0,  # PLANTA
        0.5,  # ELECTRICO
        1.0,  # PSIQUICO
        1.0,  # HIELO
        1.0,  # DRAGON
        1.0,  # SINIESTRO
        1.0,  # HADA
    ],
    # VENENO
    [
        1.0,  # NORMAL
        1.0,  # LUCHA
        1.0,  # VOLADOR
        0.5,  # VENENO
        0.5,  # TIERRA
        0.5,  # ROCA
        1.0,  # BICHO
        0.5,  # FANTASMA
        0.0,  # ACERO
        1.0,  # FUEGO
        1.0,  # AGUA
        2.0,  # PLANTA
        1.0,  # ELECTRICO
        1.0,  # PSIQUICO
        1.0,  # HIELO
        1.0,  # DRAGON
        1.0,  # SINIESTRO
        2.0,  # HADA
    ],
    # TIERRA
    [
        1.0,  # NORMAL
        1.0,  # LUCHA
        0.0,  # VOLADOR
        2.0,  # VENENO
        1.0,  # TIERRA
        2.0,  # ROCA
        0.5,  # BICHO
        1.0,  # FANTASMA
        2.0,  # ACERO
        2.0,  # FUEGO
        1.0,  # AGUA
        0.5,  # PLANTA
        2.0,  # ELECTRICO
        1.0,  # PSIQUICO
        1.0,  # HIELO
        1.0,  # DRAGON
        1.0,  # SINIESTRO
        1.0,  # HADA
    ],
    # ROCA
    [
        1.0,  # NORMAL
        0.5,  # LUCHA
        2.0,  # VOLADOR
        1.0,  # VENENO
        0.5,  # TIERRA
        1.0,  # ROCA
        2.0,  # BICHO
        1.0,  # FANTASMA
        0.5,  # ACERO
        2.0,  # FUEGO
        1.0,  # AGUA
        1.0,  # PLANTA
        1.0,  # ELECTRICO
        1.0,  # PSIQUICO
        2.0,  # HIELO
        1.0,  # DRAGON
        1.0,  # SINIESTRO
        1.0,  # HADA
    ],
    # BICHO
    [
        1.0,  # NORMAL
        0.5,  # LUCHA
        0.5,  # VOLADOR
        0.5,  # VENENO
        1.0,  # TIERRA
        1.0,  # ROCA
        1.0,  # BICHO
        0.5,  # FANTASMA
        0.5,  # ACERO
        0.5,  # FUEGO
        1.0,  # AGUA
        2.0,  # PLANTA
        1.0,  # ELECTRICO
        2.0,  # PSIQUICO
        1.0,  # HIELO
        1.0,  # DRAGON
        2.0,  # SINIESTRO
        0.5,  # HADA
    ],
    # FANTASMA
    [
        0.0,  # NORMAL
        1.0,  # LUCHA
        1.0,  # VOLADOR
        1.0,  # VENENO
        1.0,  # TIERRA
        1.0,  # ROCA
        1.0,  # BICHO
        2.0,  # FANTASMA
        1.0,  # ACERO
        1.0,  # FUEGO
        1.0,  # AGUA
        1.0,  # PLANTA
        1.0,  # ELECTRICO
        2.0,  # PSIQUICO
        1.0,  # HIELO
        1.0,  # DRAGON
        0.5,  # SINIESTRO
        1.0,  # HADA
    ],
    # ACERO
    [
        1.0,  # NORMAL
        1.0,  # LUCHA
        1.0,  # VOLADOR
        1.0,  # VENENO
        1.0,  # TIERRA
        2.0,  # ROCA
        1.0,  # BICHO
        1.0,  # FANTASMA
        0.5,  # ACERO
        0.5,  # FUEGO
        0.5,  # AGUA
        1.0,  # PLANTA
        0.5,  # ELECTRICO
        1.0,  # PSIQUICO
        2.0,  # HIELO
        1.0,  # DRAGON
        1.0,  # SINIESTRO
        2.0,  # HADA
    ],
    # FUEGO
    [
        1.0,  # NORMAL
        1.0,  # LUCHA
        1.0,  # VOLADOR
        1.0,  # VENENO
        1.0,  # TIERRA
        0.5,  # ROCA
        2.0,  # BICHO
        1.0,  # FANTASMA
        2.0,  # ACERO
        0.5,  # FUEGO
        0.5,  # AGUA
        2.0,  # PLANTA
        1.0,  # ELECTRICO
        1.0,  # PSIQUICO
        2.0,  # HIELO
        0.5,  # DRAGON
        1.0,  # SINIESTRO
        1.0,  # HADA
    ],
    # AGUA
    [
        1.0,  # NORMAL
        1.0,  # LUCHA
        1.0,  # VOLADOR
        1.0,  # VENENO
        2.0,  # TIERRA
        2.0,  # ROCA
        1.0,  # BICHO
        1.0,  # FANTASMA
        1.0,  # ACERO
        2.0,  # FUEGO
        0.5,  # AGUA
        0.5,  # PLANTA
        1.0,  # ELECTRICO
        1.0,  # PSIQUICO
        1.0,  # HIELO
        0.5,  # DRAGON
        1.0,  # SINIESTRO
        1.0,  # HADA
    ],
    # PLANTA
    [
        1.0,  # NORMAL
        1.0,  # LUCHA
        0.5,  # VOLADOR
        0.5,  # VENENO
        2.0,  # TIERRA
        2.0,  # ROCA
        0.5,  # BICHO
        1.0,  # FANTASMA
        0.5,  # ACERO
        0.5,  # FUEGO
        2.0,  # AGUA
        0.5,  # PLANTA
        1.0,  # ELECTRICO
        1.0,  # PSIQUICO
        1.0,  # HIELO
        0.5,  # DRAGON
        1.0,  # SINIESTRO
        1.0,  # HADA
    ],
    # ELECTRICO
    [
        1.0,  # NORMAL
        1.0,  # LUCHA
        2.0,  # VOLADOR
        1.0,  # VENENO
        0.0,  # TIERRA
        1.0,  # ROCA
        1.0,  # BICHO
        1.0,  # FANTASMA
        1.0,  # ACERO
        1.0,  # FUEGO
        2.0,  # AGUA
        0.5,  # PLANTA
        0.5,  # ELECTRICO
        1.0,  # PSIQUICO
        1.0,  # HIELO
        0.5,  # DRAGON
        1.0,  # SINIESTRO
        1.0,  # HADA
    ],
    # PSIQUICO
    [
        1.0,  # NORMAL
        2.0,  # LUCHA
        1.0,  # VOLADOR
        2.0,  # VENENO
        1.0,  # TIERRA
        1.0,  # ROCA
        1.0,  # BICHO
        1.0,  # FANTASMA
        0.5,  # ACERO
        1.0,  # FUEGO
        1.0,  # AGUA
        1.0,  # PLANTA
        1.0,  # ELECTRICO
        0.5,  # PSIQUICO
        1.0,  # HIELO
        1.0,  # DRAGON
        0.0,  # SINIESTRO
        1.0,  # HADA
    ],
    # HIELO
    [
        1.0,  # NORMAL
        1.0,  # LUCHA
        2.0,  # VOLADOR
        1.0,  # VENENO
        2.0,  # TIERRA
        1.0,  # ROCA
        1.0,  # BICHO
        1.0,  # FANTASMA
        0.5,  # ACERO
        0.5,  # FUEGO
        0.5,  # AGUA
        2.0,  # PLANTA
        1.0,  # ELECTRICO
        1.0,  # PSIQUICO
        0.5,  # HIELO
        2.0,  # DRAGON
        1.0,  # SINIESTRO
        1.0,  # HADA
    ],
    # DRAGON
    [
        1.0,  # NORMAL
        1.0,  # LUCHA
        1.0,  # VOLADOR
        1.0,  # VENENO
        1.0,  # TIERRA
        1.0,  # ROCA
        1.0,  # BICHO
        1.0,  # FANTASMA
        0.5,  # ACERO
        1.0,  # FUEGO
        1.0,  # AGUA
        1.0,  # PLANTA
        1.0,  # ELECTRICO
        1.0,  # PSIQUICO
        1.0,  # HIELO
        2.0,  # DRAGON
        1.0,  # SINIESTRO
        0.0,  # HADA
    ],
    # SINIESTRO
    [
        1.0,  # NORMAL
        0.5,  # LUCHA
        1.0,  # VOLADOR
        1.0,  # VENENO
        1.0,  # TIERRA
        1.0,  # ROCA
        1.0,  # BICHO
        2.0,  # FANTASMA
        1.0,  # ACERO
        1.0,  # FUEGO
        1.0,  # AGUA
        1.0,  # PLANTA
        1.0,  # ELECTRICO
        2.0,  # PSIQUICO
        1.0,  # HIELO
        1.0,  # DRAGON
        0.5,  # SINIESTRO
        0.5,  # HADA
    ],
    # HADA
    [
        1.0,  # NORMAL
        2.0,  # LUCHA
        1.0,  # VOLADOR
        0.5,  # VENENO
        1.0,  # TIERRA
        1.0,  # ROCA
        1.0,  # BICHO
        1.0,  # FANTASMA
        0.5,  # ACERO
        0.5,  # FUEGO
        1.0,  # AGUA
        1.0,  # PLANTA
        1.0,  # ELECTRICO
        1.0,  # PSIQUICO
        1.0,  # HIELO
        2.0,  # DRAGON
        2.0,  # SINIESTRO
        1.0,  # HADA
    ],
]
