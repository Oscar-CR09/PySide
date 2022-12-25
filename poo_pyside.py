import sys
from PySide6.QtWidgets import QMainWindow, QApplication


class VentanaPySide():
    def __init__(self):
        self.ventana = QMainWindow()
        self.ventana.setWindowTitle('POO con PySide')
        self.ventana.resize(600, 400)


if __name__ =='__main__':
    app = QApplication([])
    #creamos objeto de tipo ventana 
    ventana1 = VentanaPySide()
    ventana1.ventana.show()
    #Ejecutamos la ventana
    sys.exit(app.exec())