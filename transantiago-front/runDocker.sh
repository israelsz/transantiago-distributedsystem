#!/bin/bash

sudo docker stop ctr_distribuidos-frontend
sudo docker rm ctr_distribuidos-frontend
sudo docker rmi img_distribuidos-frontend

sudo docker build -t img_distribuidos-frontend:latest .
sudo docker run --network="host" --name ctr_distribuidos-frontend -d img_distribuidos-frontend