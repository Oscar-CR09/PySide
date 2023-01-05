from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor, QAction, QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QLabel, QToolBar, QStatusBar, QCheckBox,QDialog,QDialogButtonBox


class VentanaDialogo(QDialog):
    def __init__(self,padre=None):
        super().__init__(padre)
        self.setWindowTitle('Ventana de Dialogo')
        #Agregamos un boton de aceptar y otro de cancelar
        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.botones_dialogo = QDialogButtonBox(botones)
        self.botones_dialogo.accepted.connect(self.accept)
        self.botones_dialogo.rejected.connect(self.reject)

        #se crea un layout para publicar los botones
        self.layout = QVBoxLayout()
        mensaje = QLabel('Preciona alguno de los botones ')
        self.layout.addWidget(mensaje)
        self.layout.addWidget(self.botones_dialogo)
        self.setLayout(self.layout)



class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos')
        #agragamos un boton 
        boton = QPushButton('Mostrar dialogo')
        boton.clicked.connect(self.click_boton)

        #Publicamos el boton
        self.setCentralWidget(boton)

    def click_boton(self,s):
        print(f'Click sobre boton: {s}')
        #Creamos el dialogo

        dialogo = VentanaDialogo(self)

        valor_retornado = dialogo.exec()
        print(f'valor retornado: {valor_retornado}')

        if valor_retornado:
            print('se precionado OK')

        else:
            print('Se preciono Cancel')

            

        '''
        dialogo = QDialog(self)
        dialogo.setWindowTitle('Ayuda')
        #se crea un nuevo event loop
        #se bloquea la ventana padre (ventana modal)
        #y solo podemos interactura con la nueva ventana 
        #Para ejecutar la ventana modal
        dialogo.exec()
        '''
 
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
