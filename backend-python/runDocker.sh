# Creación backend
docker rmi distribuidos-backend-spark
docker build -t distribuidos-backend-spark .
docker stop "spark_backend"
docker rm -f "spark_backend"
#Cargar variables
source .env
docker run -d --name "spark_backend" --network="host" distribuidos-backend-spark