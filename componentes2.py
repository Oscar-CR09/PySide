import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('componentes')
        self.setFixedSize(800, 600)
        # creamos un componente de tipo etiqueta (Label)
        etiqueta = QLabel('Hola')
        etiqueta.setPixmap(QPixmap('imagen2.jpg'))
        etiqueta.setScaledContents(True)
        self.setCentralWidget(etiqueta)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
    # sys.exit(app.exec())
