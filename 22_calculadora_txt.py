"""
EJERCICIO 22: CALCULADORA .TXT
 Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
resultado e imprímelo.
   - El .txt se corresponde con las entradas de una calculadora.
   - Cada línea tendrá un número o una operación representada por un
     símbolo (alternando ambos).
   - Soporta números enteros y decimales.
   - Soporta las operaciones suma "+", resta "-", multiplicación "*"
    y división "/".
   - El resultado se muestra al finalizar la lectura de la última
    línea (si el .txt es correcto).
   - Si el formato del .txt no es correcto, se indicará que no se han
    podido resolver las operaciones.
"""

def calculadora_txt():
    try:
        with open("Challenge21.txt", "r") as fichero:
            lineas = fichero.readlines()
        
        # Elimina los espacios en blanco y filtra las líneas vacías
        lineas = [line.strip() for line in lineas if line.strip()]
        
        if not lineas:
            print("El archivo está vacío.")
            return

        # Inicializa el resultado con el primer número
        result = float(lineas[0])
        
        # Recorre el resto de las líneas
        for i in range(1, len(lineas), 2):
            operador = lineas[i]
            if i + 1 >= len(lineas):
                print("Formato incorrecto: falta un número después del operador.")
                return
            
            numero = float(lineas[i + 1])
            
            if operador == "+":
                result += numero
            elif operador == "-":
                result -= numero
            elif operador == "*":
                result *= numero
            elif operador == "/":
                if numero == 0:
                    print("Error: División por cero.")
                    return
                result /= numero
            else:
                print(f"Formato incorrecto: operador desconocido '{operador}'.")
                return
        
        print(f"Resultado: {result}")
    
    except FileNotFoundError:
        print("El archivo 'Challenge21.txt' no se encontró.")
    except ValueError:
        print("Formato incorrecto: se esperaba un número.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


calculadora_txt()