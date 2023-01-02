import sys
from PySide6.QtCore import Qt
# from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox, QComboBox, QListWidget,QLineEdit


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('componentes')
        linea_texto = QLineEdit()
        # este componete se publica
        self.setCentralWidget(linea_texto)
        #Establecemos el maximo de caracteres a capturar
        linea_texto.setMaxLength(15)
        #se establece un texto de ayuda
        linea_texto.setPlaceholderText('Establece tu nombre')
        #solo lectura
        #linea_texto.setReadOnly(True)
        #validacion mask
        linea_texto.setInputMask('00-0000-0000')
        #Evento enter cambio de selccion detexto cambio texto 
        linea_texto.returnPressed.connect(self.enter_precionado)
        linea_texto.selectionChanged.connect(self.cambio_seleccion)
        linea_texto.textChanged.connect(self.cambio_texto)


    def enter_precionado(self):
        print('Se preciono el enter')
        self.centralWidget().setText('00-0000-0000')


    def cambio_seleccion(self):
        print('Cambio selccion de texto ')
        print(self.centralWidget().selectedText())

    def cambio_texto(self,nuevo_texto):
        print('cambio de texto')
        print(nuevo_texto)

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
    # sys.exit(app.exec())
