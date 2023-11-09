import sys
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QPushButton, QListWidget,QMainWindow
from PyQt5 import uic

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Estructura_Mejorada.ui', self)
        
        '''
        Esto el lo que hace que se inicialize.
        '''
        self.init()

    def init(self):
        self.btCargar.clicked.connect(self.ui_cargar_clp)
        self.bt_Prueba.clicked.connect(self.ui_prueba_clp)
    
    def ui_cargar_clp(self):
        self.txt_basura.setText('Joan es tonto')
    def ui_prueba_clp(self):
        self.txt_prueba.setText('Prueba')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = UI()
    ventana.show()

    sys.exit(app.exec_())
