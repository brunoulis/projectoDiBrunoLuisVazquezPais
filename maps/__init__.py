import sys

from os import system

from PySide6.QtWidgets import QApplication

from controllers.MainUI import MainUI

"""
Programa python con pyside
sera una interfaz con 4 text edits en los que meteremos los datos que enviaremos el qtwebview del maps para buscar la ruta
también podremos guardarlo en lista para seleccionarlo y pasarlo al webview
""" 

if (__name__ == "__main__"):
    app = QApplication()
    
    Interfaz = MainUI()
    Interfaz.show()
    
    sys.exit(app.exec())