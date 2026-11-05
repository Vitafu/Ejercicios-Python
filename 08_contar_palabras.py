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

def contar_palabras(text: str) -> dict:
    # Pasa a minúsculas, extrae las palabras (letras y dígitos) y cuenta cuántas veces aparece cada una
    return dict(Counter(re.findall(r"\w+", text.lower())))

# Devuelve un diccionario {palabra: veces}, en el orden de primera aparición
print(contar_palabras("Hola, mi nombre es victor. Mi nombre completo es Victor Pedreira (Vitafu)."))  
print(contar_palabras("Hola hola mundo"))  
print(contar_palabras("a b c"))            
