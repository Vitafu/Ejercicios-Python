"""
EJERCICIO 6: ASPECT RATIO DE UNA IMAGEN
Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.
   - Url de ejemplo:
     https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
   - Por ratio hacemos referencia por ejemplo a los "16:9" de una
     imagen de 1920*1080px.
"""

from math import gcd

def aspect_ratio(ancho: int, alto: int) -> str:
    divisor = gcd(ancho, alto)
    return f"{ancho // divisor}:{alto // divisor}"

print(aspect_ratio(1920, 1080))  # 16:9
print(aspect_ratio(800, 600))    # 4:3
print(aspect_ratio(1000, 1000))  # 1:1
