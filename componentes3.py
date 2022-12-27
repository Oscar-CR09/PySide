import sys
from PySide6.QtCore import Qt
#from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication,QCheckBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('componentes')
        #creamos un nuevo componente checkbox
        checkbox = QCheckBox('Este es un Checkbox')
        #se activa el tercer estado 
        #se tiene tres estados 0 apagado 1. sin estado 2. encendido
        checkbox.setTristate(True)
        #conectar la señal de componente 
        checkbox.stateChanged.connect(self.mostrar_estado)
        #este componete se publica
        self.setCentralWidget(checkbox)

    def mostrar_estado(self, estado):
        print('estado checkbox:', estado)
        #se trabaja con las constantes
        if estado == Qt.Checked:
            print('Checkbox encendido')
        elif estado == Qt.PartiallyChecked:
            print('Checkbox sin estado o parcialmente checado')
        elif estado == Qt.Unchecked:
            print('Checkbox apagado')
        else:
            print('Checkbox con estado invalido')


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
    # sys.exit(app.exec())
