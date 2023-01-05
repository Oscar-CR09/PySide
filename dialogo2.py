from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor, QAction, QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QLabel, QToolBar, QStatusBar, QCheckBox, QDialog, QDialogButtonBox,QMessageBox




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
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle('Dialogo con pregunta')
        dialogo.setText('Ventana dialogo con pregunta')
        # se agrega los botones
        dialogo.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #se agrega un icono a la ventana dialogo
        dialogo.setIcon(QMessageBox.Question)
        valor_retornado = dialogo.exec()
        #imprimir el valor retornado
        print(f'Valor retornado: {valor_retornado}')
        if valor_retornado == QMessageBox.Yes:
            print('Regreso el valor Yes (SI)')

        else:
            print('Regreso un valor distinto de No ')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
