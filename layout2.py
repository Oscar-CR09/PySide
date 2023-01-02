from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout,QHBoxLayout


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
        #layout vertical
        #layout horizontal
        #layout = QVBoxLayout()
        layout = QHBoxLayout()
        #Agregar un nuevo componente 
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        #crear un componente generico para poder publicar layou 
        componente = QWidget()
        componente.setLayout(layout)

        self.setCentralWidget(componente)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
