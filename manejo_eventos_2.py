# signals y slots
import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signal y Slots')
        # Boton
        self.boton = QPushButton('Click aqui')
        # Asociamos la señal de click al slot evento click
        self.boton.clicked.connect(self.evento_click)
        #conecatar a la señal de cambio de titulo 
        self.windowTitleChanged.connect(self.cambio_titulo_aplicacion)
        # Publicamos al boton
        self.setCentralWidget(self.boton)

    def evento_click(self):
        #cambiar el textodel boton y el titulo de la ventana 
        self.boton.setText('Nuevo texto boton')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo titulo de la aplicacion ')
        print('Evento click')

    def cambio_titulo_aplicacion(self,nuevotitulo):
        print(f'NUevotitulo aplicacion: {nuevotitulo}')


if __name__ == '__main__':
    # Creamos el objeto aplicaion
    app = QApplication([])
    # creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
