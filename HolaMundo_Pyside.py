import sys
from PySide6.QtWidgets import QApplication, QWidget,QPushButton,QMainWindow


#Clase base de Qt (PySide)
# se encarga de procesar los eventos (event loop)
app = QApplication()
#cualquier componente puede ser una ventana en Pyside
#crear un objeto ventana 
#ventana = QWidget()
#ventana = QPushButton('Boton PySide')
ventana = QMainWindow()

#se agrega el titulo
ventana.setWindowTitle('Hola mundo con PySide')
#se modifica el tamaño de la ventana 
ventana.resize(600, 400)
#mostrar la ventana
ventana.show()
#Se ejecuta la aplicacion 
sys.exit(app.exec())