"""
EJERCICIO 18: LA CARRERA DE OBSTÁCULOS
Crea una función que evalúe si un/a atleta ha superado correctamente una
carrera de obstáculos.
   - La función recibirá dos parámetros:
        - Un array que sólo puede contener String con las palabras
          "run" o "jump"
        - Un String que represente la pista y sólo puede contener "_" (suelo)
          o "|" (valla)
   - La función imprimirá cómo ha finalizado la carrera:
        - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
          será correcto y no variará el símbolo de esa parte de la pista.
        - Si hace "jump" en "_" (suelo), se variará la pista por "x".
        - Si hace "run" en "|" (valla), se variará la pista por "/".
    - La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""

from enum import Enum

class AthleteState(Enum):
    # Estados posibles del atleta en la pista
    RUN = "_"
    JUMP = "|"

def check_race(actions, track):
    # Comprobamos que la longitud de las acciones coincida con la longitud de la pista
    if len(actions) != len(track):
        raise ValueError("The number of actions must match the length of the track.")

    track_list = list(track)
    success = True

    # Iteramos sobre las acciones y la pista para evaluar el desempeño del atleta
    for i in range(len(actions)):
        action = actions[i]
        track_segment = track_list[i]

        if action == "run" and track_segment == AthleteState.RUN.value:
            continue  # Correct action, do nothing
        elif action == "jump" and track_segment == AthleteState.JUMP.value:
            continue  # Correct action, do nothing
        elif action == "jump" and track_segment == AthleteState.RUN.value:
            track_list[i] = "x"  # Incorrect jump on ground
            success = False
        elif action == "run" and track_segment == AthleteState.JUMP.value:
            track_list[i] = "/"  # Incorrect run on hurdle
            success = False

    print("".join(track_list))
    return success

print(check_race(["run", "jump", "run", "jump", "run"], "_|_|_"))
print(check_race(["run", "run", "run", "jump", "run"], "_|_|_"))
print(check_race(["run", "run", "jump", "jump", "run"], "_|_|_"))