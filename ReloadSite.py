# coding=utf-8

import subprocess
import webbrowser

try:
    # llamo a un subproceso para ejecutar el script:
    subprocess.call("./CheckInternetCon.sh", shell=True)

    # obtengo el porcentaje de paquetes perdidos a hacer un ping (con Script CheckInternetCon.sh)
    file = open("pingData.txt", "r")
    porcentaje = int(file.read(1))    
    file.close()

    if porcentaje >= 50:
        print("Mala conexion")
    else:
        print("Buena conexion.")

except:
    print("No se pudo llamar al subproceso.")


