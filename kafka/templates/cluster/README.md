# Template Cluster

* Configurando los docker-compose es posible montar un cluster con la cantidad de instancias de zookeeper y brokers de kafka que se deseen


## Comandos para esta imagen especifica de kafka [wurstmeister]
### Crear Topic
* Para crear un topic entrar en cualquier instancia de kafka dentro de cualquier docker perteneciente al cluster 
```bash
  docker exec -it <nombre-contenedor-kafka> /bin/bash
```
* Crear un topic (la tubería): Reemplazar <direccion> por la ip de cualquier maquina que este ejecutando una instancia de kafka
* El factor de replicación se recomienda sea 2, no puede ser mayor a la cantidad de brokers (instancia de kafka) existentes en el cluster, sino tira error.
* Para el numero de particiones:
  * Si se tienen menos de 6 brokers en el cluster: el numero de particiones debe ser 3*Cantidad de brokers en el cluster.
  * Para más de 12 brokers usar: 2*Cantidad de brokers en el cluster.
  * Fuente: https://www.conduktor.io/kafka/kafka-topics-choosing-the-replication-factor-and-partitions-count/

```bash
  kafka-topics.sh --create --bootstrap-server <direccion>:9092 --topic <nombre-topic> --partitions 6 --replication-factor 2
```
### Producir mensajes desde la terminal

* Entrar en un contenedor que tenga kafka perteneciente al cluster
```bash
  docker exec -it <nombre-contenedor-kafka> /bin/bash
```
* Reemplazar <direccion> por la ip de cualquier maquina que este ejecutando una instancia de kafka
```bash
  kafka-console-producer.sh --broker-list <direccion>:9092 --topic <nombre-topic>
```

### Leer mensajes desde la terminal (consumir)

* Entrar en un contenedor que tenga kafka perteneciente al cluster
```bash
  docker exec -it <nombre-contenedor-kafka> /bin/bash
```
* Reemplazar <direccion> por la ip de cualquier maquina que este ejecutando una instancia de kafka
```bash
  kafka-console-consumer.sh --bootstrap-server <direccion> --topic <nombre-topic> --from-beginning
```
