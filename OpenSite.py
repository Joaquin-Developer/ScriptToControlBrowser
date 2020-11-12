
import webbrowser

try:
    # abr en navegador Chromium, esta abrir la página de Google
    # si llamamos al metodo open_new, se abrirá una nueva ventana de chromium
    webbrowser.get("chromium").open("https://www.google.com/")
    pass
except webbrowser.Error:
    print("No se pudo localizar chrome")
    pass

