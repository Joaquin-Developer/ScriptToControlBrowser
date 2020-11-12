# coding=utf-8

import subprocess
import webbrowser

try:
    subprocess.call("./CheckInternetCon.sh", shell=True)
    

except:
    print("No se pudo llamar al subproceso.")


