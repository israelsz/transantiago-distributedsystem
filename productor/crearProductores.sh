#!/bin/bash
source .env
echo "Datos ingresados:"
echo "IP:$IP"
echo "PORT:$PORT"
echo "TOPIC:$TOPIC"
echo "NUM_CONTENEDORES:$NUM_CONTENEDORES"
echo "NUM_HEBRAS:$NUM_HEBRAS"
# Realizar alguna acción con el número
python3 divisor.py $NUM_CONTENEDORES

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


# Se crean los nuevos contenedores
for ((i=1; i<=$NUM_CONTENEDORES; i++))
do
    contenedor="productor_$i"
    docker run -d --name "$contenedor" -e ID="$i" -e IP_KAFKA="$IP" -e PORT_KAFKA="$PORT" -e TOPIC="$TOPIC" -e NUM_HEBRAS="$NUM_HEBRAS" distribuidos-productor
done