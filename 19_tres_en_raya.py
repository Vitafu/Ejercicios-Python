"""
EJERCICIO 19: TRES EN RAYA
Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
y retorne lo siguiente:
   - "X" si han ganado las "X"
   - "O" si han ganado los "O"
   - "Empate" si ha habido un empate
   - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
    O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta.
Se podría representar con un vacío "", por ejemplo.
"""

"""
EJERCICIO 19: TRES EN RAYA
Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
y retorne lo siguiente:
   - "X" si han ganado las "X"
   - "O" si han ganado los "O"
   - "Empate" si ha habido un empate
   - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
    O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta.
Se podría representar con un vacío "", por ejemplo.
"""

# Comprueba el estado de un tablero de tres en raya.
def tres_en_raya(tablero):
    if len(tablero) != 3:
        return "NULL"

    casillas = []
    contador_x = 0
    contador_o = 0

    for fila in tablero:
        if len(fila) != 3:
            return "NULL"

        for casilla in fila:
            casillas.append(casilla)

            if casilla == "X":
                contador_x += 1
            elif casilla == "O":
                contador_o += 1

    # No puede haber más de una diferencia entre X y O por turno
    if abs(contador_x - contador_o) > 1:
        return "NULL"

    # Posiciones que forman líneas ganadoras: filas, columnas y diagonales
    lineas = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas
        (0, 4, 8), (2, 4, 6)              # diagonales
    ]

    gana_x = False
    gana_o = False

    for a, b, c in lineas:
        if casillas[a] == casillas[b] == casillas[c]:
            if casillas[a] == "X":
                gana_x = True
            elif casillas[a] == "O":
                gana_o = True

    if gana_x and gana_o:
        return "NULL"  # No es posible que ambos ganen
    if gana_x:
        return "X"
    if gana_o:
        return "O"
    return "DRAW"


# Pruebas
print(tres_en_raya([
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "O", "X"]
]))  # Gana X

print(tres_en_raya([
    ["-", "O", "X"],
    ["-", "X", "O"],
    ["-", "O", "X"]
]))  # Empate

print(tres_en_raya([
    ["O", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]))  # Gana O

print(tres_en_raya([
    ["X", "O", "X"],
    ["X", "X", "O"],
    ["X", "X", "X"]
]))  # Tablero inválido
