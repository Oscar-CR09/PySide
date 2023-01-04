from PySide6.QtCore import  Qt,QSize
from PySide6.QtGui import QPalette, QColor,QAction,QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QLabel,QToolBar,QStatusBar,QCheckBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra de Herramientas')

        #Etiqueta
        etiqueta = QLabel('Hola')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)

        #crear la barra de herramientas
        barra = QToolBar('Mi barra de herramientas')
        barra.setIconSize(QSize(16,16))
        #configuracion para mostrar la barra de herramientas
        #barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        #barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        #barra.setToolButtonStyle(Qt.ToolButtonIconOnly)
        #barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)


        self.addToolBar(barra)


        #agregamos un elemento a nuestra barra de herramientas
        boton_nuevo = QAction(QIcon('nuevo.png'),'Nuevo', self)
        #agregamos el boton a la barra
        barra.addAction(boton_nuevo)
        #barra de estado
        self.setStatusBar(QStatusBar(self))
        #mostrar mensaje del boton de accion 
        boton_nuevo.setStatusTip('Nuevo archivo')
        #asociasr el evento click
        boton_nuevo.triggered.connect(self.click_boton_nuevo)

        #se hace checable el boton 
        #boton_nuevo.setCheckable(True)

        #agregamos la opcion guardar 
        boton_guardar = QAction(QIcon('guardar.png'), 'Guardar', self)
        barra.addAction(boton_guardar)

        boton_guardar.setStatusTip('Guardar Archivo')
        boton_guardar.triggered.connect(self.click_boton_guardar)

        barra.addSeparator()
        barra.addWidget(QCheckBox())
        barra.addWidget(QLabel('Salir'))

        menu = self.menuBar()
        menu_archivo = menu.addMenu('&Archivo')
        menu_archivo.addAction(boton_nuevo)

        

    def click_boton_nuevo(self,s):
        print(f'NUevo Archivo click {s}')

    def click_boton_guardar(self,s):
        print(f'Guardando archivo ..... {s}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
