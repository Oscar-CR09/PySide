from random import randint
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor, QAction, QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QLabel, QToolBar, QStatusBar, QCheckBox, QDialog, QDialogButtonBox, QMessageBox, QLineEdit, QMenu


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Contextual')
        # mostrar y conectar al menu
        self.show()
        # nos conectamos ala señal de CustomcontexMenureques
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.mostrar_menu_contexto)


    def mostrar_menu_contexto(self, posicion):
        menu_contextual = QMenu(self)
        boton_nuevo = QAction(QIcon('nuevo.png'), 'Nuevo', self)
        boton_guardar = QAction(QIcon('guardar.png'), 'Guardar ', self)
        boton_salir = QAction('Salir', self)
        # conectar con la opcion triggered
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_salir.triggered.connect(self.click_boton_salir)
        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addAction(boton_salir)
        # se recupera la posicion del cursos como posicion global de la ventana padre
        # Y se ejecuta el menu contextual
        menu_contextual.exec(self.mapToGlobal(posicion))

    def click_boton_nuevo(self, s):
        print('opcion nuevo... ')

    def click_boton_guardar(self, s):
        print('opcion guardar... ')

    def click_boton_salir(self, s):
        print('opcion salir... ')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
