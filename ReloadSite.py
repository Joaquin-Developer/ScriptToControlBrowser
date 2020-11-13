# coding=utf-8

import subprocess
import webbrowser
import pandas
import selenium
from selenium.webdriver import Chrome

#from selenium.webdriver.support

driver = Chrome()

def checkInternetConnextion():
    porcentaje = 100
    try:
        # llamo a un subproceso para ejecutar el script:
        subprocess.call("./CheckInternetCon.sh", shell=True)    
    except:
        print("Error al llamar al subproceso.")
        pass

    try:
        # obtengo el porcentaje de paquetes perdidos a hacer un ping (con Script CheckInternetCon.sh)
        file = open("pingData.txt", "r")
        porcentaje = int(file.read(1))    
        file.close()
        pass
    except:
        print("Error al leer archivo.")
        pass

    return porcentaje
    pass

def reloadPage():
    # solo recargo la pagina si hay buena conexion
    if checkInternetConnextion() <= 25:
        print("recargar ...")



reloadPage();

