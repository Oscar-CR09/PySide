import sys
from PySide6.QtCore import Qt
# from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox, QComboBox, QListWidget


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('componentes')
        #componete QListWidget se parece al comobox
        lista = QListWidget()
        #agregamos elementos 
        lista.addItem('uno')
        lista.addItems(['dos','tres'])
        #monitoreamos el cambio seleccionado tanto el elemento con el texto 
        lista.currentItemChanged.connect(self.cambio_elemento)
        lista.currentTextChanged.connect(self.cambio_texto)

        # este componete se publica
        self.setCentralWidget(lista)

    def cambio_elemento(self, nuevo_elemento):
        print(f'Nuevo elemento seleccionado: {nuevo_elemento.text()} ')

    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto seleccionado: {nuevo_texto}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
    # sys.exit(app.exec())
