"""
EJERCICIO 23: CONJUNTOS
Crea una función que reciba dos array, un booleano y retorne un array.
   - Si el booleano es verdadero buscará y retornará los elementos comunes
    de los dos array.
   - Si el booleano es falso buscará y retornará los elementos no comunes
    de los dos array.
   - No se pueden utilizar operaciones del lenguaje que
    lo resuelvan directamente.
"""

def conjuntos(lista1, lista2, comunes: bool):
    resultado = []
    if comunes:
        for elemento in lista1:
            if elemento in lista2 and elemento not in resultado:
                resultado.append(elemento)
    else:
        for elemento in lista1:
            if elemento not in lista2 and elemento not in resultado:
                resultado.append(elemento)
        for elemento in lista2:
            if elemento not in lista1 and elemento not in resultado:
                resultado.append(elemento)

    return resultado


a = ["Python", "Kotlin", "PHP"]
b = ["Python", "C++", "Rust"]

print(conjuntos(a, b, True))   # ['Python']
print(conjuntos(a, b, False))  # ['Kotlin', 'PHP', 'C++', 'Rust']