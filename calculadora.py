from random import randint
from PySide6.QtCore import Qt, QSize
from functools import partial
from PySide6.QtGui import QPalette, QColor, QAction, QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QLabel, QToolBar, QStatusBar, QCheckBox, QDialog, QDialogButtonBox, QMessageBox, QLineEdit, QMenu


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora ')
        self.setFixedSize(250,250)
        self.componente_general =QWidget(self)
        self.setCentralWidget(self.componente_general)
        #creamos un layout principal
        self.layout_principal = QVBoxLayout()
        self.componente_general.setLayout( self.layout_principal)
        #metodos para crear la parte visual de la calculadora 
        self._crear_area_captura()
        #se agraga los botones
        self._crear_botone()
        #se conecta las señalaes con los slot
        self._conectar_botones()


    def _crear_area_captura(self):
        self.linea_entrada = QLineEdit()
        #Modificamos algunas propiedades
        self.linea_entrada.setFixedHeight(35)
        self.linea_entrada.setAlignment(Qt.AlignRight)
        self.linea_entrada.setReadOnly(True)
        #se agrega la linea de entrada al alyout principal
        self.layout_principal.addWidget(self.linea_entrada)



    def _crear_botone(self):
        #se crea un diccionario para definir cada boton el texto del boton con la posicion 
        self.botones = {}
        layout_botones = QGridLayout()
        # Texto | Pocicion en el grid layout
        self.botones = {
            '7':(0,0),
            '8':(0,1),
            '9':(0,2),
            '/':(0,3),
            '4':(1,0),
            '5':(1,1),
            '6':(1,2),
            '*':(1,3),
            '1':(2,0),
            '2':(2,1),
            '3':(2,2),
            '-':(2,3),
            '0':(3,0),
            '.':(3,1),
            'c':(3,2),
            '+':(3,3),
            '=':(3,4)

        }

        #se crea los botones y se agraga al grid layout
        #La posicion es un atupal de valores(rengon columnas)

        for texto_boton, posicion in self.botones.items():
            self.botones[texto_boton]=QPushButton(texto_boton)
            self.botones[texto_boton].setFixedSize(40,40)
            #se publica el boton en el grid layout
            layout_botones.addWidget(self.botones[texto_boton], posicion[0],posicion[1])

        #se agraga el laou t de botones al layout principal
        self.layout_principal.addLayout(layout_botones)

    def _conectar_botones(self):
        #recorrer cada boton del diccionario (Key - values (texto - PuhsButton))

        for texto_boton, boton in self.botones.items():
            if texto_boton not in {'=','c'}:
                #boton.clicked.connect(lambda: self._contruir_exprecion(texto_boton))
                boton.clicked.connect(partial(self._contruir_exprecion, texto_boton))
            #si conectamos el boton de limpiar 
            self.botones['c'].clicked.connect(self._limpiar_linea_entrada)
            #se conecta el boton igal
            self.botones['='].clicked.connect(self._calcular_resultado)
            self.linea_entrada.returnPressed.connect(self._calcular_resultado)

    def _contruir_exprecion(self,texto_boton):
        exprecion = self.obtener_texto() + texto_boton 
        #Actualizar la extrepcion 
        self.actualizar_texto(exprecion)

    def obtener_texto( self):
        return self.linea_entrada.text()

    def actualizar_texto(self, texto):
        self.linea_entrada.setText(texto)
        self.linea_entrada.setFocus()

    def _limpiar_linea_entrada(self):
        self.actualizar_texto('')

    def _calcular_resultado(self):
        resultado = self._evaluar_exprecion(self.obtener_texto())
        self.actualizar_texto(resultado)

    def _evaluar_exprecion(self,exprecion):
        try :
            #se utiliza la eval para evaluar exprecion
            resultado = str(eval(exprecion))

        except Exception as e :
            resultado = 'Ocurrio un error'

        return resultado





if __name__ == '__main__':
    app = QApplication()
    calculadora = Calculadora()
    calculadora.show()
    app.exec()
