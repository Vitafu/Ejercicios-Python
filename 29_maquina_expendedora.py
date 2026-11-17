"""
EJERCICIO 29: MÁQUINA EXPENDEDORA
Simula el funcionamiento de una máquina expendedora creando una operación
que reciba dinero (array de monedas) y un número que indique la selección
del producto.
   - El programa retornará el nombre del producto y un array con el dinero
    de vuelta (con el menor número de monedas).
   - Si el dinero es insuficiente o el número de producto no existe,
    deberá indicarse con un mensaje y retornar todas las monedas.
   - Si no hay dinero de vuelta, el array se retornará vacío.
   - Para que resulte más simple, trabajaremos en céntimos con monedas
    de 5, 10, 50, 100 y 200.
   - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""

from enum import Enum

# En esta clase definimos los billetes que va a aceptar la máquina
class Dinero(Enum):
   CINCO = 5
   DIEZ = 10
   CINCUENTA = 50
   CIEN = 100
   DOSCIENTOS = 200

def maquina(codigo, dinero):
   
    # Productos disponibles
    productos = {
        1: ("Agua", 30),
        3: ("Coca-Cola", 70),
        5: ("Cerveza", 135),
        7: ("Pizza", 210),
        9: ("Donut", 85)
   }

    # Comprobamos que exista el producto
    if codigo in productos:
        nombre, precio = productos[codigo]

        # Sumamos el valor
        dinero_total = 0
        for moneda in dinero:
            dinero_total += moneda.value

        # Si no hay dinero suficiente, se devuelve aviso con error
        if dinero_total < precio:
            return (f"El producto con código [{codigo}] tiene un coste {precio}. Has introducido {dinero_total}.", dinero)

        # Calculamos el cambio   
        dinero_pendiente = dinero_total - precio

        # Devolvemos el producto y el cambio
        return(nombre, devolver_dinero(dinero_pendiente))

   # Si el código no existe, avisamos y devolvemos el dinero tal cual
    return (f"El producto con código [{codigo}] no existe.", dinero)

def devolver_dinero(dinero_pendiente, dinero=None):

    # Creamos una lista mediante None
    if dinero is None:
        dinero = []

    # Caso base: no queda cambio pendiente
    if  dinero_pendiente == 0:
        return dinero

    nuevo_dinero_pendiente = dinero_pendiente
    nuevo_dinero = list(dinero)  # Copia de la lista para no modificar la original

    # Recorremos las monedas de mayor a menor valor
    for moneda in reversed(list(Dinero)):
        # Cogemos la moneda de mayor cantidad que cabe en el cambio
        if moneda.value <= dinero_pendiente:
            nuevo_dinero_pendiente -= moneda.value
            nuevo_dinero.append(moneda)
            break 

    # Caso recursivo: repetimos con el cambio que aún queda por devolver
    return devolver_dinero(nuevo_dinero_pendiente, nuevo_dinero)

print(maquina(1, [Dinero.CINCO, Dinero.CINCO, Dinero.DIEZ, Dinero.DIEZ, Dinero.DIEZ, Dinero.CINCO]))
print(maquina(3, [Dinero.DOSCIENTOS, Dinero.CINCO, Dinero.DIEZ, Dinero.DIEZ, Dinero.DIEZ, Dinero.CINCO]))
print(maquina(7, [Dinero.DIEZ, Dinero.DIEZ, Dinero.DIEZ, Dinero.DIEZ, Dinero.DIEZ, Dinero.CIEN, Dinero.CIEN]))
print(maquina(5, [Dinero.DOSCIENTOS]))