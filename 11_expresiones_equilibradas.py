"""
EJERCICIO 11: EXPRESIONES EQUILIBRADAS
Crea un programa que comprueba si los paréntesis, llaves y corchetes
de una expresión están equilibrados.
  - Equilibrado significa que estos delimitadores se abren y cierran
    en orden y de forma correcta.
  - Paréntesis, llaves y corchetes son igual de prioritarios.
    No hay uno más importante que otro.
  - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
  - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""


def main():
    print(is_balanced("{a + b [c] * (2x2)}}}}"))             # False
    print(is_balanced("{ [ a * ( c + d ) ] - 5 }"))          # True
    print(is_balanced("{ a * ( c + d ) ] - 5 }"))            # False
    print(is_balanced("{a^4 + (((ax4)}"))                    # False
    print(is_balanced("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"))  # False
    print(is_balanced("{{{{{{(}}}}}}"))                      # False
    print(is_balanced("(a"))                                 # False


# Comprueba que cada "{", "[" o "(" se cierre con su pareja y en el orden correcto.
def is_balanced(expression: str) -> bool:

    # Cada símbolo que abre y el que lo cierra.
    pairs = {"{": "}", "[": "]", "(": ")"}

    # Los símbolos que cierran.
    closers = "}])"

    # Aquí se guardan los símbolos abiertos que todavía no se han cerrado.
    stack = []

    for character in expression:

        # Si el carácter abre, se guarda en la pila.
        if character in pairs:
            stack.append(character)

        # Si el carácter cierra, hay que comprobarlo.
        elif character in closers:

            # Si no hay nada abierto, se está cerrando algo que no existe.
            if len(stack) == 0:
                return False

            # Saca el último símbolo abierto y mira si es la pareja de este.
            last_opened = stack.pop()
            if pairs[last_opened] != character:
                return False

    # Si no queda nada abierto, todo estaba bien cerrado.
    return len(stack) == 0