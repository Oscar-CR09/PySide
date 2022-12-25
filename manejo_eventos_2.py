# signals y slots
import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signal y Slots')
        # Boton
        boton = QPushButton('Click aqui')
        # conectamos el evento checado(por defaul es false)

        # Publicamos al boton
        self.setCentralWidget(boton)



if __name__ == '__main__':
    # Creamos el objeto aplicaion
    app = QApplication([])
    # creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
