"""
EJERCICIO 33: EL SEGUNDO
Dado un listado de números, encuentra el SEGUNDO más grande
"""

def segundo_mas_grande(números: list):
    if len(números) < 2:
        return None
    
    # Elimina los números duplicados
    números = list(set(números))

    # Ordena los números en orden descendente
    números.sort(reverse=True)

    # Si la lista tiene menos de 2 elementos después de eliminar duplicados, no hay un segundo más grande 
    if len(números) < 2:
        return None

    # Accede al segundo elemento de la lista ordenada y saca el segundo más grande
    return números[1]  
    

print(segundo_mas_grande([1, 2, 3, 4, 5]))
print(segundo_mas_grande([8, 14, 39, 45, 14]))
print(segundo_mas_grande([1, 1, 1, 1]))
print(segundo_mas_grande([10]))