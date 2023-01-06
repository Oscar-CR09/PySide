from random import randint
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor, QAction, QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QLabel, QToolBar, QStatusBar, QCheckBox, QDialog, QDialogButtonBox, QMessageBox,QLineEdit


class NuevaVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Python')
        layout = QVBoxLayout()
        self.etiqueta = QLabel(f'Nuevo Ventana: {randint(0,100)}')
        layout.addWidget(self.etiqueta)
        self.setLayout(layout)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nueva_ventan = NuevaVentana()
        self.setWindowTitle('Ventana')
        self.boton = QPushButton('Mostrar/ocultar nueva ventana')
        self.boton.clicked.connect(self.mostrar_nueva_ventana)
        #definimos una entrada de texto
        self.entrada_texto = QLineEdit()
        self.entrada_texto.textChanged.connect(self.nueva_ventan.etiqueta.setText)
        #layout
        layout = QVBoxLayout()
        layout.addWidget(self.boton)
        layout.addWidget(self.entrada_texto)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def mostrar_nueva_ventana(self, estado):
        if self.nueva_ventan.isVisible():
            self.nueva_ventan.hide()

        else:
            self.nueva_ventan.show()


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
