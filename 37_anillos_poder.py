"""
EJERCICIO 37: LOS ANILLOS DE PODER
¡La Tierra Media está en guerra! En ella lucharán razas leales
a Sauron contra otras bondadosas que no quieren que el mal reine
sobre sus tierras.
Cada raza tiene asociado un "valor" entre 1 y 5:
 - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
   Númenóreanos (4), Elfos (5)
 - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
   Huargos (3), Trolls (5)
Crea un programa que calcule el resultado de la batalla entre
los 2 tipos de ejércitos:
 - El resultado puede ser que gane el bien, el mal, o exista un empate.
   Dependiendo de la suma del valor del ejército y el número de integrantes.
 - Cada ejército puede estar compuesto por un número de integrantes variable
   de cada raza.
 - Tienes total libertad para modelar los datos del ejercicio.
 Ej: 1 Peloso pierde contra 1 Orco
    2 Pelosos empatan contra 1 Orco
    3 Pelosos ganan a 1 Orco
"""
from enum import Enum

class Ejercito_bondadoso(Enum):
    PELOSO = 1
    SUREÑO_BONDO = 2
    ENANO = 3
    NUMENOREANO = 4
    ELFO = 5

class Ejercito_malvado(Enum):
    SUREÑO_MALO = 2
    ORCO = 2
    GOBLIN = 2
    HUARGO = 3
    TROLL = 5

def batalla(ejercito_bondadoso, ejercito_malvado):
    suma_bondadoso = sum(ejercito_bondadoso.values())
    suma_malvado = sum(ejercito_malvado.values())
    
    if suma_bondadoso > suma_malvado:
        return "Gana el bien"
    elif suma_bondadoso < suma_malvado:
        return "Gana el mal"
    else:
        return "Empate"

print(batalla({Ejercito_bondadoso.PELOSO: 3, Ejercito_bondadoso.ELFO: 1}, {Ejercito_malvado.ORCO: 2}))  # Gana el bien
print(batalla({Ejercito_bondadoso.PELOSO: 1}, {Ejercito_malvado.ORCO: 1}))  # Empate
print(batalla({Ejercito_bondadoso.PELOSO: 1}, {Ejercito_malvado.ORCO: 2}))  # Gana el mal