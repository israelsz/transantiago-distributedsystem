# Crear la imagen del consumidor
#docker rmi distribuidos-consumidor-spark
#docker build -t distribuidos-consumidor-spark .

source .env
echo "Datos ingresados:"
echo "IP:$IP"
echo "PORT:$PORT"
echo "TOPIC:$TOPIC"
echo "IP_MONGO:$IP_MONGO"
echo "PORT_MONGO:$PORT_MONGO"




#docker stop "spark_consumidor"
#docker rm -f "spark_consumidor"
#docker run --name "spark_consumidor" -e IP_KAFKA="$IP" -e PORT_KAFKA="$PORT" -e TOPIC="$TOPIC" -e IP_MONGO="$IP_MONGO" -e PORT_MONGO="$PORT_MONGO"  distribuidos-consumidor-spark