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

        #se agrega segunda opcion
        menu_archivo.addAction(boton_guardar)

        #se agraga un separador
        menu_archivo.addSeparator()

        boton_salir = QAction('Salir',self)
        menu_archivo.addAction(boton_salir)

        #submenu menuayuda
        boton_acerca_de = QAction(QIcon('acerca.png'), 'Acerca De', self)
        menu_ayuda = menu.addMenu('Ayuda')
        menu_ayuda.addAction(boton_acerca_de)

        boton_acerca_de.triggered.connect(self.click_boton_acerca_de)

        #se agraga un submenu 
        menu_archivo.addMenu(menu_ayuda)

        #creacion de atajos para el menu
        #ejemplo combinacion de teclado 
        #boton_nuevo.setShortcut(QKeySequence('Ctrl+n'))
        boton_nuevo.setShortcut(Qt.CTRL + Qt.Key_N)
        #atajo de acerca de control + 1
        boton_acerca_de.setShortcut(Qt.CTRL + Qt.Key_1)
        #atajo de guardar control + g
        boton_guardar.setShortcut(Qt.CTRL + Qt.Key_G)


    def click_boton_acerca_de(self,s):
        print(f'Acerca de... {s}')

    def click_boton_nuevo(self,s):
        print(f'NUevo Archivo click {s}')

    def click_boton_guardar(self,s):
        print(f'Guardando archivo ..... {s}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
