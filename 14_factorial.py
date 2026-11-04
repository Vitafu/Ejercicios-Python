"""
EJERCICIO 14: FACTORIAL RECURSIVO
Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.
"""

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1

    return numero * factorial(numero-1)

print(factorial(5))