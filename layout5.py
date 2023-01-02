from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton


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
        #se define el layout
        layout_principal = QVBoxLayout()
        layout_botones = QHBoxLayout()
        self.layout_tipo_apilado = QStackedLayout()
        #se agraga los layout hijos al principal
        layout_principal.addLayout(layout_botones)
        layout_principal.addLayout(self.layout_tipo_apilado)
        #se crean los botones 

        boton_rojo = QPushButton('Rojo')
        #publicar el layout de los botones 
        layout_botones.addWidget(boton_rojo)
        #se publica el color roj 
        self.layout_tipo_apilado.addWidget(Color('red'))
        #se conecta el evento pressed del boton respectivo
        boton_rojo.pressed.connect(lambda: self.activar_tabulador(0))

        #se crea el boton azul
        boton_azul = QPushButton('Azul')
        layout_botones.addWidget(boton_azul)
        self.layout_tipo_apilado.addWidget(Color('blue'))
        # se crea el boton azul
        boton_azul.pressed.connect(lambda:self.activar_tabulador(1))

        boton_amarillo = QPushButton('Amarillo')
        layout_botones.addWidget(boton_amarillo)
        self.layout_tipo_apilado.addWidget(Color('yellow'))
        boton_amarillo.pressed.connect(lambda:self.activar_tabulador(2))


        componente = QWidget()
        componente.setLayout(layout_principal)
        self.setCentralWidget(componente)

    def activar_tabulador(self,indice):
        self.layout_tipo_apilado.setCurrentIndex(indice)
        print(f'indice seleccionado {indice}')


'''
    def activar_color_rojo(self):
        self.layout_tipo_apilado.setCurrentIndex(0)
        
    def activar_color_azul(self):
        self.layout_tipo_apilado.setCurrentIndex(1)

    def activar_color_amarillo(self):
        self.layout_tipo_apilado.setCurrentIndex(2)
'''

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
