import json
import sys
import shutil

CARPETA = 'partes'

def vaciar_carpeta():
    # Eliminar recursivamente todos los archivos y subdirectorios dentro de la carpeta
    shutil.rmtree(CARPETA)
    shutil.os.mkdir(CARPETA)
def divide_json(file_name, number):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)

    total_elements = len(data)
    elements_per_file = total_elements // number

    for i in range(number):
        start_index = i * elements_per_file
        end_index = start_index + elements_per_file
        if i == number - 1:  # último archivo puede contener elementos adicionales
            end_index = total_elements

        file_path = f'files/file{i + 1}.json'
        with open(file_path, 'w') as output_file:
            json.dump(data[start_index:end_index], output_file, indent=4)

    print(f'Se han generado {number} archivos.')
# Ejemplo de uso
if len(sys.argv) < 2:
    print("Debes proporcionar un número como argumento.")
    sys.exit(1)

numero = int(sys.argv[1])
# Realizar alguna acción con el número
vaciar_carpeta()
divide_json('paraderos.json', numero)
