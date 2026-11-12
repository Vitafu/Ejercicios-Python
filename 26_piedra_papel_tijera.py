"""
EJERCICIO 26: PIEDRA, PAPEL, TIJERA
Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""

def piedra_papel_tijera(partidas):

    # Se define un diccionario que indica qué jugada vence a cuál
    vence_a = {"ROCK": "SCISSORS", "SCISSORS": "PAPER", "PAPER": "ROCK"}

    # Contadores de las partidas que ha ganado cada jugador
    victorias_jugador1 = 0
    victorias_jugador2 = 0

    # Se recorre la lista de partidas, que contiene pares de jugadas
    for jugada1, jugada2 in partidas:

        # Si la jugada del jugador 1 vence a la del jugador 2, gana el jugador 1
        if vence_a[jugada1] == jugada2:
            victorias_jugador1 += 1
        # Si la jugada del jugador 2 vence a la del jugador 1, gana el jugador 2
        elif vence_a[jugada2] == jugada1:
            victorias_jugador2 += 1
        # Si no ocurre ninguna de las dos, es empate y no se suma nada

    # Comparo cuántas ha ganado cada uno
    if victorias_jugador1 > victorias_jugador2:
        return "Player 1"
    elif victorias_jugador2 > victorias_jugador1:
        return "Player 2"
    else:
        return "Tie"


print(piedra_papel_tijera([("ROCK", "ROCK")]))        # Tie
print(piedra_papel_tijera([("ROCK", "SCISSORS")]))    # Player 1
print(piedra_papel_tijera([("PAPER", "SCISSORS")]))   # Player 2
print(piedra_papel_tijera([("ROCK", "ROCK"), ("SCISSORS", "SCISSORS"), ("PAPER", "PAPER")]))   # Tie
print(piedra_papel_tijera([("ROCK", "SCISSORS"), ("SCISSORS", "PAPER"), ("SCISSORS", "ROCK")]))   # Player 1
print(piedra_papel_tijera([("ROCK", "PAPER"), ("SCISSORS", "ROCK"), ("PAPER", "SCISSORS")]))   # Player 2