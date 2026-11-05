"""
EJERCICIO 20: CONVERSOR DE TIEMPO
Crea una función que reciba días, horas, minutos y segundos (como enteros)
y retorne su resultado en milisegundos.
"""

def conversor_tiempo (dias: int, horas: int, minutos: int, segundos: int):
    # 1 dia son: 24 horas * 60 minutos * 60 segundos * 1000 milisegundos
    dia_mili = dias * 24 * 60 * 60 * 1000
    horas_mili = horas * 60 * 60 * 1000
    minutos_mili = minutos * 60 * 1000
    segundos_mili = segundos * 1000

    milisegundos = (dia_mili + horas_mili + minutos_mili + segundos_mili)

    return milisegundos


print(conversor_tiempo(18, 9, 32, 54))