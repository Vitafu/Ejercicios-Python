"""
EJERCICIO 24: MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
que calcule el mínimo común múltiplo (mcm) de dos números enteros.
   - No se pueden utilizar operaciones del lenguaje que
    lo resuelvan directamente.
"""

def maximo_comun_divisor(a, b):
    """Devuelve el máximo común divisor de a y b guardando sus divisores en listas."""

    # Solo funciona con enteros positivos
    if a <= 0 or b <= 0:
        raise ValueError("Los dos números deben ser mayores que 0")

    # Divisores de a (los números que lo dividen sin dejar resto)
    divisores_a = []
    for i in range(1, a + 1):
        if a % i == 0:
            divisores_a.append(i)

    # Divisores de b
    divisores_b = []
    for i in range(1, b + 1):
        if b % i == 0:
            divisores_b.append(i)

    # Divisores comunes (los que están en las dos listas)
    comunes = []
    for d in divisores_a:
        if d in divisores_b:
            comunes.append(d)

    
    return max(comunes)


def minimo_comun_multiplo(a, b):
    """Devuelve el mínimo común múltiplo de a y b guardando sus múltiplos en listas."""

    # Solo funciona con enteros positivos
    if a <= 0 or b <= 0:
        raise ValueError("Los dos números deben ser mayores que 0")

    # Múltiplos de a hasta a*b
    multiplos_a = []
    for i in range(1, b + 1):
        multiplos_a.append(a * i)

    # Múltiplos de b hasta a*b
    multiplos_b = []
    for i in range(1, a + 1):
        multiplos_b.append(b * i)

    # Múltiplos comunes (los que están en las dos listas)
    comunes = []
    for m in multiplos_a:
        if m in multiplos_b:
            comunes.append(m)

    # El menor de los múltiplos comunes es el mínimo común múltiplo
    return min(comunes)


print(maximo_comun_divisor(12, 18))  # 6
print(maximo_comun_divisor(8, 15))   # 1
print(maximo_comun_divisor(20, 5))   # 5

print(minimo_comun_multiplo(4, 6))   # 12
print(minimo_comun_multiplo(3, 5))   # 15