import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPySide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('POO con PySide')
        #self.resize(600, 400)
        #<colocamos los valores de ancho y alto fijos
        self.setFixedSize(QSize(600, 400))
        #creamos algunos componentes
        self._agregar_componentes()

    def _agregar_componentes(self):
        #agregamos un menu
        menu =self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        #agregamos algunos opciones al menu 
        accion_nuevo = QAction('Nuevo',self)
        menu_archivo.addAction(accion_nuevo)
        #agregar un texto a a barra de estado 
        accion_nuevo.setStatusTip('Nuevo archivo')
        #agregamos un mensaje a la barra de estado 
        self.statusBar().showMessage('INformacion de la barra de estado...')
        #agregamos un boton 
        boton =QPushButton('Nuevo Boton ')
        #Publicacmos el boton en la ventana 
        self.setCentralWidget(boton)

if __name__ == '__main__':
    app = QApplication([])
    # creamos objeto de tipo ventana
    ventana = VentanaPySide()
    ventana.show()
    # Ejecutamos la ventana
    sys.exit(app.exec())
