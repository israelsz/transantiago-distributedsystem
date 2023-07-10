for i in {1..15}
do
    contenedor="productor_$i"
    docker rm -f "$contenedor"
done