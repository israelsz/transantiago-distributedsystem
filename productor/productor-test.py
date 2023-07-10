import threading
import requests
import json
import time
from time import sleep
from json import dumps
from kafka import KafkaProducer
import os



# Numero de ciclos
num_ciclos = 1

# lista_terminados[i] = 0 aun no se realiza
# lista_terminados[i] = 1 tarea completada
# lista_terminados[i] = -1 fallo tarea
def imprimir_progreso():
    total_tareas = len(lista_terminados)
    while True:
        exitosas = lista_terminados.count(1)
        fallidas = lista_terminados.count(-1)
        completadas = exitosas + fallidas
        print(f"Ciclo:{num_ciclos}, Tareas completadas: {completadas} / {total_tareas}, exitosas: {exitosas}, fallidas: {fallidas}")
        time.sleep(5)


def enviar_peticion(url):
    try:
        response = requests.get(url)
        if response.status_code == 500:
            return -1
        data = response.json()
        producer.send(topico, value=data)
        return 1
    except:
        time.sleep(5)
        return enviar_peticion(url)

def mi_funcion(paraderos):
    for paradero in paraderos:
        url = f'https://www.red.cl/predictor/prediccion?t=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODYwODM2MDIxNzB9._dvYqkeUAXkYh1sppBK7djoEAR-2ucoNvpI6t8nubzk&codsimt={paradero}&codser='
        resultado = enviar_peticion(url)
        indice = lista_completa.index(paradero)
        lista_terminados[indice] = resultado



# BLOQUE PRINCIPAL
# LECTURA DE VARIABLES DE ENTORNO
id = 1
num_hebras = 10
ip_kafka = "144.22.52.73"
port_kafka = "9093"
topico = "macrohard"
# Abre el archivo JSON que le corresponde
with open(f'parte{id}.json') as file:
    # Lee el contenido del archivo
    lista_completa = json.load(file)
# Lista encargada de registrar el progreso
lista_terminados = [0] * len(lista_completa)

# SE CONECTA A KAFKA
servidor = f"{ip_kafka}:{port_kafka}"
producer = KafkaProducer(
    bootstrap_servers=[servidor],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

# Calcular el tamaño de cada segmento
tamanio_segmento = len(lista_completa) // num_hebras

# Se crea hebra encargada del progreso
t = threading.Thread(target=imprimir_progreso)
t.start()



while True:
    # Crear y ejecutar las hebras
    hebras = []
    for i in range(num_hebras):
        inicio = i * tamanio_segmento
        fin = inicio + tamanio_segmento if i < num_hebras - 1 else len(lista_completa)
        lista_segmentada = lista_completa[inicio:fin]
        t = threading.Thread(target=mi_funcion, args=(lista_segmentada,))
        t.start()
        hebras.append(t)
    # Esperar a que todas las hebras terminen
    for t in hebras:
        t.join() 
    # Aumenta el numero de ciclos terminados
    num_ciclos += 1
    # Se limpia la lista de terminados
    lista_terminados = [0] * len(lista_completa)
