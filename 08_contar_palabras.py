"""
EJERCICIO 8: CONTANDO PALABRAS
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
   - Los signos de puntuación no forman parte de la palabra.
   - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
   - No se pueden utilizar funciones propias del lenguaje que
     lo resuelvan automáticamente.

"""

import re
from collections import Counter

def count_words(text: str) -> dict:
    # Pasa a minúsculas, extrae las palabras (letras y dígitos) y cuenta cuántas veces aparece cada una
    return dict(Counter(re.findall(r"\w+", text.lower())))

# Devuelve un diccionario {palabra: veces}, en el orden de primera aparición
print(count_words("Hola, mi nombre es victor. Mi nombre completo es Victor Pedreira (Vitafu)."))  # {'hola': 1, 'mi': 2, 'nombre': 2, 'es': 2, 'victor': 2, 'completo': 1, 'pedreira': 1, 'vitafu': 1}
print(count_words("Hola hola mundo"))  # {'hola': 2, 'mundo': 1}
print(count_words("a b c"))            # {'a': 1, 'b': 1, 'c': 1}