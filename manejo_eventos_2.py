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
        boton.setCheckable(True)
        # conectamos otro slot al evento checar
        boton.clicked.connect(self.event_chechar)
        # conectamos el evento signal click con el slot (evento_click)
        boton.clicked.connect(self.evento_click)

        # Publicamos al boton
        self.setCentralWidget(boton)

    def event_chechar(self, checar):
        self.boton_checado = checar
        print('Checado', self.boton_checado)

    def evento_click(self):
        print('Has hecho click')
        # accedemos al boton checado
        print('boton checado desde evento click', self.boton_checado)


if __name__ == '__main__':
    # Creamos el objeto aplicaion
    app = QApplication([])
    # creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
