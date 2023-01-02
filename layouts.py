from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget ,QApplication,QMainWindow


class Color(QWidget):
    def __init__(self,nuevo_color):
        super().__init__()
        #indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        #Creamos el componente de color de fondo aplicando el nuevo color 
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        #aplicamos el nuevo color al componente 
        self.setPalette(paletaColores)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layout en PySide')
        componente_color_fondo = Color('red')
        #componete se expande para cubrir el tamaño disponible
        self.setCentralWidget(componente_color_fondo)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()