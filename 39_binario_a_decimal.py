"""
EJERCICIO 39: BINARIO A DECIMAL
Crea un programa se encargue de transformar un número binario
a decimal sin utilizar funciones propias del lenguaje que
lo hagan directamente.
"""

def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)
    
    for i in range(longitud):
        bit = int(binario[longitud - 1 - i])  # Tomamos el bit desde el final
        decimal += bit * (2 ** i)  # Convertimos a decimal
    
    return decimal

print(binario_a_decimal("1010"))  # 10
print(binario_a_decimal("1111"))  # 15
print(binario_a_decimal("1000"))  # 8