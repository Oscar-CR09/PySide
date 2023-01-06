from random import randint
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor, QAction, QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QLabel, QToolBar, QStatusBar, QCheckBox, QDialog, QDialogButtonBox, QMessageBox, QLineEdit



class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eventos')
        self.etiqueta = QLabel('Da click en esta ventana')
        self.setCentralWidget(self.etiqueta)


    def mouseMoveEvent(self, event):
        #self.etiqueta.setText('Evento mouseMoveEvent detectado')
        #preguntamos por el evento del mouse que lanza el evento
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('mouseMoveEvent Boton Izquierdo')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('mouseMoveEvent Boton Central')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('mouseMoveEvent Boton Derecho')


    def mousePressEvent(self, event):
        #self.etiqueta.setText('Evento mousePressEvent detectado')
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('mousePressEvent Boton Izquierdo')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('mousePressEvent Boton Central')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('mousePressEvent Boton Derecho')


    def mouseReleaseEvent(self, event):
        #self.etiqueta.setText('Evento mouseReleaseEvent detectado')
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('mousePressEvent Boton Izquierdo')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('mousePressEvent Boton Central')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('mousePressEvent Boton Derecho')


    def mouseDoubleClickEvent(self, event):
        #self.etiqueta.setText('Evento mouse DoubleclickEvent detectado ')
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('DoubleclickEvent Boton Izquierdo')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('DoubleclickEvent Boton Central')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('DoubleclickEvent Boton Derecho')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
