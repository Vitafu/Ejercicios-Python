"""
EJERCICIO 21: PARANDO EL TIEMPO
Crea una función que sume 2 números y retorne su resultado pasados
unos segundos.
   - Recibirá por parámetros los 2 números a sumar y los segundos que
    debe tardar en finalizar su ejecución.
   - Si el lenguaje lo soporta, deberá retornar el resultado de forma
    asíncrona, es decir, sin detener la ejecución del programa principal.
    Se podría ejecutar varias veces al mismo tiempo.
"""

import time

def parando_tiempo(num1: int, num2: int, espera: int):
    suma = num1 + num2

    # Pausa el programa los segundos indicados
    time.sleep(espera)

    print(f"La suma es {suma}. El tiempo de espera han sido {espera} segundos")

parando_tiempo(5, 6, 3)