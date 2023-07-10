#!/bin/bash

# Solicitar al usuario que ingrese un número
read -p "En cuantos contenedores dividir los paraderos: " numero
# Realizar alguna acción con el número
python3 divisor.py $numero

# Se construye la imagen de docker
docker rmi distribuidos-productor
docker build -t distribuidos-productor .

# Se borran los contenedores que habian
for i in {1..10}
do
    contenedor="productor_$i"
    docker rm -f "$contenedor"
done

#Numero de hebras para cada contenedor
read -p "Cuantas hebras por cada contendor: " numHebras
read -p "IP de kafka: " ip
read -p "Puerto de kafka: " port
read -p "Topico: " topic

# Se crean los nuevos contenedores
for ((i=1; i<=$numero; i++))
do
    contenedor="productor_$i"
    docker run -d --name "$contenedor" -e ID="$i" -e IP_KAFKA="$ip" -e PORT_KAFKA="$port" -e TOPIC="$topic" -e NUM_HEBRAS="$numHebras" distribuidos-productor
done