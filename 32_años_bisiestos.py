"""
EJERCICIO 32: AÑOS BISIESTOS
Crea una función que imprima los 30 próximos años bisiestos
siguientes a uno dado.
   - Utiliza el menor número de líneas para resolver el ejercicio.
"""

def años_bisiestos(año: int):
    
    # Año que se está comprobando
    año_actual = año + 1

    # Almacenamos los años bisiestos encontrados
    contador_años = 0


    # Repetimos la comprobación hasta encontrar 30 años bisiestos
    while contador_años < 30:
        
        # Comprobamos que el año es bisiesto
        if año_actual % 4 == 0 and (año_actual % 100 != 0 or año_actual % 400 == 0):
            print (año_actual)

            # Añadimos un año al contador
            contador_años += 1

        # Pasa al siguiente año sea o no bisiesto
        año_actual += 1


años_bisiestos(1999)