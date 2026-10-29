"""
EJERCICIO 5: ÁREA DE UN POLÍGONO
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
   - La función recibirá por parámetro sólo UN polígono a la vez.
   - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
   - Imprime el cálculo del área de un polígono de cada tipo.

"""

def area_triangulo(base: float, altura: float) -> float:
    return base * altura / 2

def area_rectangulo(largo: float, ancho: float) -> float:
    return largo * ancho

def area_cuadrado(lado: float) -> float:
    return lado ** 2

print(area_triangulo(10, 5))   # 25.0
print(area_rectangulo(5, 7))   # 35
print(area_cuadrado(4))        # 16