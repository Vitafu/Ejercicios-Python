"""
EJERCICIO 27: CUADRADO Y TRIANGULO 2D
Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
   - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
   - EXTRA: ¿Eres capaz de dibujar más figuras?
"""


def dibujar(tamano, figura):

    if figura == "cuadrado":
        # Imprime tantos asteriscos como se indica en el tamaño
        for fila in range(tamano):
            print("* " * tamano)

    elif figura == "triangulo":
        # range(1, tamano + 1) va de 1 hasta tamano, incluido.
        for fila in range(1, tamano + 1):
            print("* " * fila)

    else:
        # Si no se imprimen ninguna de las dos figuras, salta este mensaje
        print("No sé dibujar esa figura")


dibujar(5, "cuadrado")
print("")
dibujar(5, "triangulo")