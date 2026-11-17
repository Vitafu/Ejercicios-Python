"""
EJERCICIO 30: ORDENA LA LISTA
Crea una función que ordene y retorne una matriz de números.
   - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
    adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
    o de mayor a menor.
   - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
    automáticamente.
"""


def ordenar_lista(lista, parametro: bool):

    # Hacemos una copia de la lista para no modificar la original
    lista_ordenada = lista.copy()

    # Obtenemos la longitud de la lista
    n = len(lista_ordenada)

    # Si el parámetro es True, ordenamos de menor a mayor, si es False, de mayor a menor
    if parametro == True:
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista_ordenada[j] > lista_ordenada[j+1]:
                    lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
    # Si el parámetro es False, ordenamos de mayor a menor
    else:
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista_ordenada[j] < lista_ordenada[j+1]:
                    lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]

    return lista_ordenada
         

print(ordenar_lista([4, 90, 17, 45, 23, 78], True))
print(ordenar_lista([4, 90, 17, 45, 23, 78], False))
