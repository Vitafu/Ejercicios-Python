"""
EJERCICIO 38: LANZAMIENTO DE ZELDA
¡Han anunciado un nuevo "The Legend of Zelda"!
Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
"The Legend of Zelda" de la historia?
Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
que tú selecciones.
    - Debes buscar cada uno de los títulos y su día de lanzamiento 
    (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
"""

class JuegoZelda:
    SELECTOR = {
        "The Legend of Zelda": "21/02/1986",
        "Zelda II: The Adventure of Link": "14/01/1987",
        "The Legend of Zelda: A Link to the Past": "21/11/1991",
        "The Legend of Zelda: Link's Awakening": "06/06/1993",
        "The Legend of Zelda: Ocarina of Time": "21/11/1998",
        "The Legend of Zelda: Majora's Mask": "27/04/2000",
        "The Legend of Zelda: Oracle of Seasons": "27/02/2001", 
    }

def calcular_diferencia(juego1, juego2):
    from datetime import datetime

    fecha1 = datetime.strptime(JuegoZelda.SELECTOR[juego1], "%d/%m/%Y")
    fecha2 = datetime.strptime(JuegoZelda.SELECTOR[juego2], "%d/%m/%Y")

    diferencia = abs(fecha2 - fecha1)
    años = diferencia.days // 365
    dias = diferencia.days % 365

    return años, dias

print(calcular_diferencia("The Legend of Zelda", "The Legend of Zelda: Ocarina of Time"))