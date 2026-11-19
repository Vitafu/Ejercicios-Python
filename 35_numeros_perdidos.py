"""
EJERCICIO 35: LOS NÚMEROS PERDIDOS
Dado un array de enteros ordenado y sin repetidos,
crea una función que calcule y retorne todos los que faltan entre
el mayor y el menor.
  - Lanza un error si el array de entrada no es correcto.

"""

def numeros_perdidos(array):
    if not isinstance(array, list) or len(array) == 0:
        raise ValueError("El array debe ser una lista no vacía.")
    
    if any(not isinstance(x, int) for x in array):
        raise ValueError("Todos los elementos del array deben ser enteros.")
    
    if sorted(array) != array:
        raise ValueError("El array debe estar ordenado de menor a mayor.")
    
    if len(array) != len(set(array)):
        raise ValueError("El array no debe contener elementos repetidos.")
    
    min_num = array[0]
    max_num = array[-1]
    
    return [num for num in range(min_num, max_num + 1) if num not in array]


print(numeros_perdidos([1, 2, 4, 6]))  # Salida: [3, 5]
print(numeros_perdidos([5, 6, 7, 8]))  # Salida: []
print(numeros_perdidos([9, 7, 5, 3, 1]))  # Lanza un error: El array debe estar ordenado de menor a mayor.
print(numeros_perdidos([1, 2, 2, 3]))  # Lanza un error: El array no debe contener elementos repetidos.
print(numeros_perdidos([]))  # Lanza un error: El array debe ser una lista no vacía.
print(numeros_perdidos([1, '2', 3]))  # Lanza un error: Todos los elementos del array deben ser enteros.