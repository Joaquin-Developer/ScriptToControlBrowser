# coding=utf-8

import webbrowser

try:
    # abrir en navegador Chromium, una nueva pestaña con la url indicada
    # si llamamos al metodo open_new, se abrirá una nueva ventana de chromium
    webbrowser.get("chromium").open("https://www.google.com/")
    pass
except webbrowser.Error:
    print("No se pudo localizar chrome")
    pass

