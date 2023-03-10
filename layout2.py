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
        #layout = QHBoxLayout()
        #anidar layout Horizontal y vertical 
        layout_horizontal =QHBoxLayout()
        #se agraga el espacio al margen 
        layout_horizontal.setContentsMargins(10, 10, 10, 10)#externo
        #se agrega un espaciode l lado horizontal 
        layout_horizontal.setSpacing(30)#interno 
        layout_vertical= QVBoxLayout()
        #Se agrea espacion en el layout vetical interna
        layout_vertical.setContentsMargins(5, 10, 5, 10)
        #se agrega un espacio dentro de un elemnetto 
        layout_vertical.setSpacing(20)
        #agregamos widget al layout vertical


        #Agregar un nuevo componente 
        layout_vertical.addWidget(Color('red'))
        layout_vertical.addWidget(Color('green'))
        layout_vertical.addWidget(Color('blue'))

        #agregar el layout veical dentro  del horizontal de maneda anidada
        layout_horizontal.addLayout(layout_vertical)
        #se agrega al layout
        layout_horizontal.addWidget(Color('yellow'))
        layout_horizontal.addWidget(Color('purple'))
        #crear un componente generico para poder publicar layou 
        componente = QWidget()
        componente.setLayout(layout_horizontal)


        self.setCentralWidget(componente)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
