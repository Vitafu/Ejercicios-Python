"""
EJERCICIO 34: SEXAGENARIO CHINO
Crea un función, que dado un año, indique el elemento 
y animal correspondiente en el ciclo sexagenario del zodíaco chino.
  - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
  - El ciclo sexagenario se corresponde con la combinación de los elementos
   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
   (en este orden).
  - Cada elemento se repite dos años seguidos.
  - El último ciclo sexagenario comenzó en 1984 (Madera Rata).

"""

def sexagenario_chino(anio):

    # Creamos listas de elementos y animales
    elementos = ["Madera", "Fuego", "Tierra", "Metal", "Agua"]
    animales = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente",
                "Caballo", "Oveja", "Mono", "Gallo", "Perro", "Cerdo"]

    # Calculamos el índice del elemento y del animal correspondiente al año dado
    indice_elemento = ((anio - 1984) // 2) % len(elementos)
    indice_animal = (anio - 1984) % len(animales)

    # Almacenamos el elemento y el animal correspondiente
    elemento = elementos[indice_elemento]
    animal = animales[indice_animal]

    return f"{elemento} {animal}"

print(sexagenario_chino(2021))