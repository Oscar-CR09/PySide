import sys
from PySide6.QtCore import Qt
# from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox, QComboBox, QListWidget, QLineEdit,QSpinBox,QDoubleSpinBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('componentes')
        #QSlider es para avalores numericos
        
        #qspinbox para valores numericos
        #numero = QSpinBox()
        #QDoubleSpinbox es para valores flotantes
        numero = QDoubleSpinBox()
        #establecer el valor minimo y el valor maximo o rango 
        #numero.setMinimum(-5)
        #numero.setMaximum(8)
        numero.setRange(-5, 8.8)
        #prefijo o subfijo
        numero.setPrefix('$')
        numero.setSuffix('c')
        #incrementos salto step
        numero.setSingleStep(.5)
        # Valu change 
        #envia el valor nuevo numerico
        numero.valueChanged.connect(self.cambio_valor)
        #envia el valor en texto incluido prefijo y subfijo
        numero.textChanged.connect(self.cambio_texto)



        #Publicamos este componente
        self.setCentralWidget(numero)

    def cambio_valor(self, nuevo_valor):
         print(f'NUevo valor: {nuevo_valor}')

    def cambio_texto (self,nuevo_texto):
         print(f'Nuevo texto: {nuevo_texto}')

   
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
    # sys.exit(app.exec())
