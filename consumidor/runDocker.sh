# Crear la imagen del consumidor
docker rmi distribuidos-consumidor-spark
docker build -t distribuidos-consumidor-spark .

read -p "IP de kafka: " ip
read -p "Puerto de kafka: " port
read -p "Topico: " topic
read -p "IP de Mongo: " ip_mongo
read -p "Puerto de Mongo: " port_mongo

docker stop "spark_consumidor"
docker rm -f "spark_consumidor"
docker run --name "spark_consumidor" -e IP_KAFKA="$ip" -e PORT_KAFKA="$port" -e TOPIC="$topic" -e IP_MONGO="$ip_mongo" -e PORT_MONGO="$port_mongo"  distribuidos-consumidor-spark

