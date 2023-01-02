import sys
from PySide6.QtCore import Qt
# from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox, QComboBox, QListWidget, QLineEdit, QSpinBox, QDoubleSpinBox, QSlider,QDial


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('componentes')
        # QDial es una rueda similar al slider pero utilizado para aplizaciones de audio 

        componente = QDial()
        componente.setRange(-5,50)
        # conectar a las señales
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_posicion)
        componente.sliderPressed.connect(self.slider_precionado)
        componente.sliderReleased.connect(self.slider_liberado)

        # Publicamos este componente
        self.setCentralWidget(componente)

    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor}')

    def slider_cambio_posicion(self, nueva_pocision):
        print(f'NUeva pocision {nueva_pocision}')

    def slider_precionado(self):
        print('Dial precionado')

    def slider_liberado(self):
        print('QDial Liberado')


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
    # sys.exit(app.exec())
