"""
EJERCICIO 2: ANAGRAMA

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
   - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
   - NO hace falta comprobar que ambas palabras existan.
   - Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(palabra1: str, palabra2: str) -> bool:
    p1 = palabra1.lower()
    p2 = palabra2.lower()
    if p1 == p2:
        return False  # una palabra no es anagrama de sí misma
    return sorted(p1) == sorted(p2)


print(anagrama("Amor", "Roma"))  # True
print(anagrama("Pola", "Roma"))  # False
print(anagrama("Roma", "roma"))  # False
