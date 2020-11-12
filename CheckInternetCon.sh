#!/bin/bash

# obtengo linea de salida del comando ping donde especifican % paquetes perdidos:
pingData=$(ping -c4 8.8.8.8 | grep loss)

# voy cortando la cadena anterior, hasta quedarme con el numero en % de paq. perdidos:
porcentaje=$(echo $linea | cut -d"," -f3 | cut -d"%" -f1)

# guardo el porcentaje obtenido en un archivo:
#touch pingData.txt
# echo $porcentaje  > pingData.txt

echo "Porcentaje= $porcentaje"