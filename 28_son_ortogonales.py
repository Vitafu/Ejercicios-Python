"""
EJERCICIO 28: VECTORES ORTOGONALES
Crea un programa que determine si dos vectores son ortogonales.
   - Los dos array deben tener la misma longitud.
   - Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""

def son_ortogonales(vector_uno, vector_dos):
    """
    Dos vectores son ortogonales si:
        (x1 * x2) + (y1 * y2) == 0
    
    """
    producto_escalar = vector_uno[0] * vector_dos[0] + vector_uno[1] * vector_dos[1]
    if producto_escalar == 0:
        return True
    else:
        return False

print(son_ortogonales((1, 2), (2, 1)))   # False
print(son_ortogonales((2, 1), (-1, 2)))  # True