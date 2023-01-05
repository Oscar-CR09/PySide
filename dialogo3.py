from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor, QAction, QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QLabel, QToolBar, QStatusBar, QCheckBox, QDialog, QDialogButtonBox, QMessageBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos')
        # agragamos un boton
        boton = QPushButton('Mostrar dialogo')
        boton.clicked.connect(self.click_boton)

        # Publicamos el boton
        self.setCentralWidget(boton)

    def click_boton(self, s):
        print(f'Click sobre boton: {s}')
        # Creamos el dialogo
        dialogo = QMessageBox.question(self, 'Pregunta', 'Ventana con pregunta')

        if dialogo == QMessageBox.Yes:
            print('Regreso el valor Yes (SI)')

        else:
            print('Regreso un valor distinto de No ')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
