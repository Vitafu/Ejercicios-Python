"""
EJERCICIO 15: NÚMERO DE AMSTRONG
Escribe una función que calcule si un número dado es un número de Armstrong
 (o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información
al respecto.
"""

def es_armstrong(numero):

    # Los números negativos no son de Armstrong
    if numero < 0:
        return False

    # Convierto el número a texto para poder ir dígito por dígito
    texto = str(numero)

    # Cuento cuántos dígitos tiene (será el exponente)
    cantidad = len(texto)

    # Aquí voy sumando
    suma = 0

    # Recorro cada dígito
    for digito in texto:
        # Lo convierto otra vez a número, lo elevo a la cantidad de dígitos y lo sumo
        suma = suma + int(digito) ** cantidad

    # Si la suma es igual al número, es de Armstrong
    if suma == numero:
        return True
    else:
        return False


print(es_armstrong(371))    # True
print(es_armstrong(-371))   # False
print(es_armstrong(372))    # False
print(es_armstrong(0))      # True