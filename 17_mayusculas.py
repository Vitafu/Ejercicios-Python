"""
EJERCICIO 17: EN MAYÚSCULAS
Crea una función que reciba un String de cualquier tipo y se encargue de
poner en mayúscula la primera letra de cada palabra.
   - No se pueden utilizar operaciones del lenguaje que
    lo resuelvan directamente.
"""

import re


def capitalize(text: str) -> str:

    # Copia del texto original, que se irá modificando palabra a palabra.
    capitalized_text = text
    
    for word in re.sub(r"[^A-zÀ-ú]", " ", text).split(" "):
        capitalized_text = capitalized_text.replace(word, word[:1].upper() + word[1:])

    return capitalized_text

print(capitalize("¿hola qué tal estás?"))
print(capitalize("¿hola      qué tal estás?"))
print(capitalize("El niño ñoño"))