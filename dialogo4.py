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
        dialogo = QMessageBox.critical(self, 'Problema Critico', 'Ventana con problema critico',buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore, defaultButton= QMessageBox.Discard)

        if dialogo == QMessageBox.Discard:
            print('Regreso el valor Discard')
        elif dialogo == QMessageBox.NoToAll :
            print('Regreso el valor de NoToAll')

        else:
            print('Regreso un valor distinto de Ignorar ')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
