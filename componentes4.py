import sys
from PySide6.QtCore import Qt
# from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox,QComboBox 


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('componentes')
        # creamos un nuevo componente combo box
        combobox = QComboBox()
        #agregar elemntos
        combobox.addItem('Uno')
        combobox.addItems(['Dos','Tres'])
        #monitoriamos el cambio seleccionado tanto como indice como texto 
        combobox.currentIndexChanged.connect(self.cambio_indice)
        combobox.currentTextChanged.connect(self.cambio_texto)


        # este componete se publica
        self.setCentralWidget(combobox)

    def cambio_indice(self, nuevo_indice):
         print(f'Nuevo indice seleccionado: {nuevo_indice} ')

    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto seleccionado: {nuevo_texto}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
    # sys.exit(app.exec())
