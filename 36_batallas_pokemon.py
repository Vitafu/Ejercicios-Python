"""
EJERCICIO 36: BATALLAS POKÉMON
Crea un programa que calcule el daño de un ataque durante
una batalla Pokémon.
  - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
  - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
  - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
   (buscar su efectividad)
  - El programa recibe los siguientes parámetros:
  - Tipo del Pokémon atacante.
  - Tipo del Pokémon defensor.
  - Ataque: Entre 1 y 100.
  - Defensa: Entre 1 y 100.
"""

from enum import Enum
from dataclasses import dataclass

class TipoPokemon(Enum):
  AGUA = "Agua"
  FUEGO = "Fuego"
  ELECTRICO = "Electrico"
  PLANTA = "Planta"


@dataclass
class Efectividad:
  efectivo: TipoPokemon
  no_efectivo: TipoPokemon

def Batalla(atacante: TipoPokemon, defensor: TipoPokemon, ataque: int, defensa: int) -> float | None:

  if ataque < 1 or ataque > 100 or defensa < 1 or defensa > 100:
    print ("El ataque o la defensa tienen valores no permitidos")
    return None

  tipos = {
    TipoPokemon.AGUA: Efectividad(TipoPokemon.FUEGO, TipoPokemon.PLANTA),
    TipoPokemon.FUEGO: Efectividad(TipoPokemon.PLANTA, TipoPokemon.AGUA),
    TipoPokemon.PLANTA: Efectividad(TipoPokemon.AGUA, TipoPokemon.FUEGO),
    TipoPokemon.ELECTRICO: Efectividad(TipoPokemon.AGUA, TipoPokemon.PLANTA),
  }

  efectivo = 1.0

  if atacante == defensor or tipos[atacante].no_efectivo == defensor:
    efectivo = 0.5
    print("No es muy efectivo")
  elif tipos[atacante].efectivo == defensor:
    efectivo = 2
    print("Es muy efectivo")
  else:
    efectivo = 1
    print("Es neutro")

  puntos = 50 * (ataque / defensa) * efectivo
  return puntos

print(Batalla(TipoPokemon.AGUA, TipoPokemon.FUEGO, 50, 30))
print(Batalla(TipoPokemon.AGUA, TipoPokemon.FUEGO, 101, -10))
print(Batalla(TipoPokemon.FUEGO, TipoPokemon.AGUA, 50, 30))
print(Batalla(TipoPokemon.FUEGO, TipoPokemon.FUEGO, 50, 30))
print(Batalla(TipoPokemon.PLANTA, TipoPokemon.ELECTRICO, 30, 50))