from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton,QTabWidget


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
        self.setWindowTitle('Tabulador en PySide')

        #Creamos el componente
        tabulador = QTabWidget()
        #Posicion de las etiquetas del tabulador
        tabulador.setTabPosition(QTabWidget.North)
        #indicamos si queremos que se muevan las etiquetas del tabulador
        tabulador.setMovable(True)
        #para que se vea similar en MacOs
        tabulador.setDocumentMode(True)

        #Agregamos los colores a cada tabulador
        tabulador.addTab(Color('red'), 'Rojo')
        tabulador.addTab(Color('yellow'), 'Amarillo')
        tabulador.addTab(Color('green'), 'Verde')   

        self.setCentralWidget(tabulador)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
