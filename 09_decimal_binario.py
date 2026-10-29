"""
EJERCICIO 9: DECIMAL A BINARIO
Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def decimal_to_binary(decimal: int) -> str:
    # Texto binario resultado, que se construye de derecha a izquierda
    binary = ""

    # Repite hasta que el número llegue a 0 (el 0 cuenta como falso)
    while decimal:
        # El resto de dividir entre 2 es el siguiente dígito, y se pone delante de los anteriores
        binary = f"{decimal % 2}{binary}"
        # División entera entre 2, que descarta los decimales
        decimal //= 2

    # Si el texto quedó vacío (solo pasa con el 0), devuelve "0"
    return binary or "0"

print(decimal_to_binary(387))  # 110000011
print(decimal_to_binary(0))    # 0