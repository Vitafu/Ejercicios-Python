"""
EJERCICIO 31: MARCO DE PALABRAS
Crea una función que reciba un texto y muestre cada palabra en una línea,
formando un marco rectangular de asteriscos.
   - ¿Qué te parece el reto? Se vería así:
    **********
    * ¿Qué   *
    * te     *
    * parece *
    * el     *
    * reto?  *
    **********
"""



def marco_palabras(texto: str):
   
   # Separamos el texto en palabras usando el espacio como separador
   palabras = texto.split(" ")

   # Medimos la longitud de las palabras y nos quedamos con la más grande
   max_length = max(len(palabra) for palabra in palabras)

   # Imprimimos la línea superior de asteriscos teniendo en cuenta la palabra más larga
   print("*" * (max_length + 4))

   for palabra in palabras:
      if palabra:
         print(f"* {palabra.ljust(max_length)} *")

   # Imprimimos la línea inferior de asteriscos, igual que la superior
   print("*" * (max_length + 4))


marco_palabras("¿Qué te parece el reto?")
marco_palabras("¿Cuántos retos de código de la comunidad has resuelto?")