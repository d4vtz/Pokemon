"""
Constantes
"""
# Base de Datos
DB_POKEDEX = "BaseDatos/Pokedex.json"
DB_ATAQUES = "BaseDatos/Ataques.json"
ATAQUES_OBJ = "BaseDatos/Ataques.obj"

# Categorias de Ataque
FISICO = "FISICO"
ESPECIAL = "ESPECIAL"
ESTADO = "ESTADO"

# Stats
HP = "HP"
ATAQUE = "Ataque"
DEFENSA = "Defensa"
ATAQUE_ESPECIAL = "Ataque Especial"
DEFENSA_ESPECIAL = "Defensa Especial"
VELOCIDAD = "Velocidad"

STATS = [HP, ATAQUE, DEFENSA, ATAQUE_ESPECIAL, DEFENSA_ESPECIAL, VELOCIDAD]

# Comandos
ATACAR = "Atacar"
SELECIONAR_ATAQUE = "Seleccionar ataque"

# Pokemons
BULBASAUR = "Bulbasaur"
IVYSAUR = "Ivysaur"
VENUSAUR = "Venusaur"
CHARMANDER = "Charmander"
CHARMELEON = "Charmeleon"
CHARIZARD = "Charizard"
SQUIRTLE = "Squirtle"
WARTORTLE = "Wartortle"
BLASTOISE = "Blastoise"
CATERPIE = "Caterpie"
METAPOD = "Metapod"
BUTTERFREE = "Butterfree"
WEEDLE = "Weedle"
KAKUNA = "Kakuna"
BEEDRILL = "Beedrill"
PIDGEY = "Pidgey"
PIDGEOTTO = "Pidgeotto"
PIDGEOT = "Pidgeot"
RATTATA = "Rattata"
RATICATE = "Raticate"
SPEAROW = "Spearow"
FEAROW = "Fearow"
EKANS = "Ekans"
ARBOK = "Arbok"
PIKACHU = "Pikachu"
RAICHU = "Raichu"
SANDSHREW = "Sandshrew"
SANDSLASH = "Sandslash"
NIDORAN_HEMBRA = "Nidoran♀"
NIDORINA = "Nidorina"
NIDOQUEEN = "Nidoqueen"
NIDORAN_MACHO = "Nidoran♂"
NIDORINO = "Nidorino"
NIDOKING = "Nidoking"
CLEFAIRY = "Clefairy"
CLEFABLE = "Clefable"
VULPIX = "Vulpix"
NINETALES = "Ninetales"
JIGGLYPUFF = "Jigglypuff"
WIGGLYTUFF = "Wigglytuff"
ZUBAT = "Zubat"
GOLBAT = "Golbat"
ODDISH = "Oddish"
GLOOM = "Gloom"
VILEPLUME = "Vileplume"
PARAS = "Paras"
PARASECT = "Parasect"
VENONAT = "Venonat"
VENOMOTH = "Venomoth"
DIGLETT = "Diglett"
DUGTRIO = "Dugtrio"
MEOWTH = "Meowth"
PERSIAN = "Persian"
PSYDUCK = "Psyduck"
GOLDUCK = "Golduck"
MANKEY = "Mankey"
PRIMEAPE = "Primeape"
GROWLITHE = "Growlithe"
ARCANINE = "Arcanine"
POLIWAG = "Poliwag"
POLIWHIRL = "Poliwhirl"
POLIWRATH = "Poliwrath"
ABRA = "Abra"
KADABRA = "Kadabra"
ALAKAZAM = "Alakazam"
MACHOP = "Machop"
MACHOKE = "Machoke"
MACHAMP = "Machamp"
BELLSPROUT = "Bellsprout"
WEEPINBELL = "Weepinbell"
VICTREEBEL = "Victreebel"
TENTACOOL = "Tentacool"
TENTACRUEL = "Tentacruel"
GEODUDE = "Geodude"
GRAVELER = "Graveler"
GOLEM = "Golem"
PONYTA = "Ponyta"
RAPIDASH = "Rapidash"
SLOWPOKE = "Slowpoke"
SLOWBRO = "Slowbro"
MAGNEMITE = "Magnemite"
MAGNETON = "Magneton"
FARFETCHD = "Farfetch'd"
DODUO = "Doduo"
DODRIO = "Dodrio"
SEEL = "Seel"
DEWGONG = "Dewgong"
GRIMER = "Grimer"
MUK = "Muk"
SHELLDER = "Shellder"
CLOYSTER = "Cloyster"
GASTLY = "Gastly"
HAUNTER = "Haunter"
GENGAR = "Gengar"
ONIX = "Onix"
DROWZEE = "Drowzee"
HYPNO = "Hypno"
KRABBY = "Krabby"
KINGLER = "Kingler"
VOLTORB = "Voltorb"
ELECTRODE = "Electrode"
EXEGGCUTE = "Exeggcute"
EXEGGUTOR = "Exeggutor"
CUBONE = "Cubone"
MAROWAK = "Marowak"
HITMONLEE = "Hitmonlee"
HITMONCHAN = "Hitmonchan"
LICKITUNG = "Lickitung"
KOFFING = "Koffing"
WEEZING = "Weezing"
RHYHORN = "Rhyhorn"
RHYDON = "Rhydon"
CHANSEY = "Chansey"
TANGELA = "Tangela"
KANGASKHAN = "Kangaskhan"
HORSEA = "Horsea"
SEADRA = "Seadra"
GOLDEEN = "Goldeen"
SEAKING = "Seaking"
STARYU = "Staryu"
STARMIE = "Starmie"
MR_MIME = "Mr. Mime"
SCYTHER = "Scyther"
JYNX = "Jynx"
ELECTABUZZ = "Electabuzz"
MAGMAR = "Magmar"
PINSIR = "Pinsir"
TAUROS = "Tauros"
MAGIKARP = "Magikarp"
GYARADOS = "Gyarados"
LAPRAS = "Lapras"
DITTO = "Ditto"
EEVEE = "Eevee"
VAPOREON = "Vaporeon"
JOLTEON = "Jolteon"
FLAREON = "Flareon"
PORYGON = "Porygon"
OMANYTE = "Omanyte"
OMASTAR = "Omastar"
KABUTO = "Kabuto"
KABUTOPS = "Kabutops"
AERODACTYL = "Aerodactyl"
SNORLAX = "Snorlax"
ARTICUNO = "Articuno"
ZAPDOS = "Zapdos"
MOLTRES = "Moltres"
DRATINI = "Dratini"
DRAGONAIR = "Dragonair"
DRAGONITE = "Dragonite"
MEWTWO = "Mewtwo"
MEW = "Mew"

POKEMON = [
    BULBASAUR,
    IVYSAUR,
    VENUSAUR,
    CHARMANDER,
    CHARMELEON,
    CHARIZARD,
    SQUIRTLE,
    WARTORTLE,
    BLASTOISE,
    CATERPIE,
    METAPOD,
    BUTTERFREE,
    WEEDLE,
    KAKUNA,
    BEEDRILL,
    PIDGEY,
    PIDGEOTTO,
    PIDGEOT,
    RATTATA,
    RATICATE,
    SPEAROW,
    FEAROW,
    EKANS,
    ARBOK,
    PIKACHU,
    RAICHU,
    SANDSHREW,
    SANDSLASH,
    NIDORAN_HEMBRA,
    NIDORINA,
    NIDOQUEEN,
    NIDORAN_MACHO,
    NIDORINO,
    NIDOKING,
    CLEFAIRY,
    CLEFABLE,
    VULPIX,
    NINETALES,
    JIGGLYPUFF,
    WIGGLYTUFF,
    ZUBAT,
    GOLBAT,
    ODDISH,
    GLOOM,
    VILEPLUME,
    PARAS,
    PARASECT,
    VENONAT,
    VENOMOTH,
    DIGLETT,
    DUGTRIO,
    MEOWTH,
    PERSIAN,
    PSYDUCK,
    GOLDUCK,
    MANKEY,
    PRIMEAPE,
    GROWLITHE,
    ARCANINE,
    POLIWAG,
    POLIWHIRL,
    POLIWRATH,
    ABRA,
    KADABRA,
    ALAKAZAM,
    MACHOP,
    MACHOKE,
    MACHAMP,
    BELLSPROUT,
    WEEPINBELL,
    VICTREEBEL,
    TENTACOOL,
    TENTACRUEL,
    GEODUDE,
    GRAVELER,
    GOLEM,
    PONYTA,
    RAPIDASH,
    SLOWPOKE,
    SLOWBRO,
    MAGNEMITE,
    MAGNETON,
    FARFETCHD,
    DODUO,
    DODRIO,
    SEEL,
    DEWGONG,
    GRIMER,
    MUK,
    SHELLDER,
    CLOYSTER,
    GASTLY,
    HAUNTER,
    GENGAR,
    ONIX,
    DROWZEE,
    HYPNO,
    KRABBY,
    KINGLER,
    VOLTORB,
    ELECTRODE,
    EXEGGCUTE,
    EXEGGUTOR,
    CUBONE,
    MAROWAK,
    HITMONLEE,
    HITMONCHAN,
    LICKITUNG,
    KOFFING,
    WEEZING,
    RHYHORN,
    RHYDON,
    CHANSEY,
    TANGELA,
    KANGASKHAN,
    HORSEA,
    SEADRA,
    GOLDEEN,
    SEAKING,
    STARYU,
    STARMIE,
    MR_MIME,
    SCYTHER,
    JYNX,
    ELECTABUZZ,
    MAGMAR,
    PINSIR,
    TAUROS,
    MAGIKARP,
    GYARADOS,
    LAPRAS,
    DITTO,
    EEVEE,
    VAPOREON,
    JOLTEON,
    FLAREON,
    PORYGON,
    OMANYTE,
    OMASTAR,
    KABUTO,
    KABUTOPS,
    AERODACTYL,
    SNORLAX,
    ARTICUNO,
    ZAPDOS,
    MOLTRES,
    DRATINI,
    DRAGONAIR,
    DRAGONITE,
    MEWTWO,
    MEW,
]
