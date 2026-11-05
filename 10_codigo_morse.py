"""
EJERCICIO 10: CÓDIGO MORSE
Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
  - Debe detectar automáticamente de qué tipo se trata y realizar
    la conversión.
  - En morse se soporta raya "—", punto ".", un espacio " " entre letras
    o símbolos y dos espacios entre palabras "  ".
  - El alfabeto morse soportado será el mostrado en
    https://es.wikipedia.org/wiki/Código_morse.
"""


MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "Ñ": "--.--", "O": "---", "P": ".--.", "Q": "--.-",
    "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",
    "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..",
}

# Diccionario al revés: de código morse a letra
TEXTO = {code: letter for letter, code in MORSE.items()}


def texto_a_morse(text: str) -> str:
    resultado = ""

    for character in text.upper():
        if character == " ":
            resultado += "/ "  # La barra separa palabras
        elif character in MORSE:
            resultado += MORSE[character] + " "  # Un espacio separa letras

    return resultado


def morse_to_text(morse: str) -> str:
    resultado = ""

    for code in morse.split(" "):
        if code == "/":
            resultado += " "
        elif code in TEXT:
            resultado += TEXT[code]

    return resultado


morse = text_to_morse("Chocapic. Es una marca de cereales?")
print(morse)           # -.-. .... --- -.-. .- .--. .. -.-. .-.-.- / . ... / ..- -. .- / -- .- .-. -.-. .- / -.. . / -.-. . .-. . .- .-.. . ... ..--..
print(morse_to_text(morse))  # CHOCAPIC. ES UNA MARCA DE CEREALES?
