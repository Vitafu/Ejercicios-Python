"""
EJERCICIO 12: ELIMINANDO CARACTERES
Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
   - out1 contendrá todos los caracteres presentes en la str1 pero NO
    estén presentes en str2.
   - out2 contendrá todos los caracteres presentes en la str2 pero NO
    estén presentes en str1.
"""

def eliminar_caracteres(str1, str2):
    # Se irán guardando las letras que cumplan la condición en estas variables
    out1 = ""
    out2 = ""

    # Recorremos la primera cadena y vamos agregando a out1 los caracteres que no estén en str2
    for letra in str1:
        # Si la letra no está en str2, la agregamos a out1
        if letra not in str2:
            out1 += letra

    # Recorremos la segunda cadena y vamos agregando a out2 los caracteres que no estén en str1
    for letra in str2:
        if letra not in str1:
            out2 += letra

    return out1, out2

str1 = "Victor"
str2 = "Pedreira"

out1, out2 = eliminar_caracteres(str1, str2)
print(f"out1: {out1}")
print(f"out2: {out2}")