from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,QGridLayout


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # aplicamos el nuevo color al componente
        self.setPalette(paletaColores)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layout en PySide')
        #layout grid
        layout = QGridLayout()
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('blue'), 0, 2)
        layout.addWidget(Color('green'), 1, 1)
        layout.addWidget(Color('yellow'), 1, 0)
        layout.addWidget(Color('purple'), 1, 2)

        componente = QWidget()
        componente.setLayout(layout)
        self.setCentralWidget(componente)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
