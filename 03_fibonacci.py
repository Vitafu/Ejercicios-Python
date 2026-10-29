"""
EJERCICIO 3: SUCESIÓN DE FIBONACCI

Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
   - La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
"""

def fibonacci():
    n0 = 0
    n1 = 1

    for _ in range(50):
        print(n0)
        n0, n1 = n1, n0 + n1

fibonacci()