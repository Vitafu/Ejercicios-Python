"""
EJERCICIO 16: ¿CUANTOS DÍAS?
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
   - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
   - La función recibirá dos String y retornará un Int.
   - La diferencia en días será absoluta (no importa el orden de las fechas).
   - Si una de las dos cadenas de texto no representa una fecha correcta se
    lanzará una excepción.
"""

from datetime import datetime

def cuantos_dias(fecha1: str, fecha2: str) -> int:
    formato = "%d/%m/%Y"
    # strptime lanza ValueError si el texto no es una fecha válida
    d1 = datetime.strptime(fecha1, formato)
    d2 = datetime.strptime(fecha2, formato)
    return abs((d2 - d1).days)


print(cuantos_dias("19/10/1999", "29/03/2010"))  # 3814
print(cuantos_dias("29/03/2010", "19/10/1999"))  # 3814 (el orden no importa)
print(cuantos_dias("31/02/2020", "01/01/2020"))  # ValueError: el 31 de febrero no existe
