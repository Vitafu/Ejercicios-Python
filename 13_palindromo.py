"""
EJERCICIO 13: ES UN PALÍNDROMO
Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
"""

def es_palindromo(texto):
    # Pasar todo a minúsculas
    texto = texto.lower()

    # Quitar las tildes
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")

    # Quedarse solo con letras y números (sin espacios ni signos)
    limpio = ""
    for letra in texto:
        if letra.isalnum():
            limpio += letra

    # Comparar el texto con el texto del revés
    return limpio == limpio[::-1]


print(es_palindromo("Ana lleva al oso la avellana."))  # True
print(es_palindromo("Hola qué tal?"))                  # False