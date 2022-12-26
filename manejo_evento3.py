# signals y slots
import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signal y Slots')
        self.setFixedSize(400,200)
        #definimos la etiqueta y linea de edicion 
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        #Conectar el widget de entrada de texto con la etiqueta
        #la señal es textCanged el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        #Publicamos los componentes usando un layout
        disposicion = QVBoxLayout()
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        #contenedorcrear
        contenedor = QWidget()
        contenedor.setLayout(disposicion)
        #publicamos el contenedor el cual ya incluyelos elementos 
        self.setCentralWidget(contenedor)



if __name__ == '__main__':
    # Creamos el objeto aplicaion
    app = QApplication([])
    # creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
