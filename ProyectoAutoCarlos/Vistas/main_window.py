# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
sys.path.append ('../Controladores')
from main_controller import *

class MainWindow (QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.controlador = MainControlador()
        self.init_ui()

    def init_ui(self):
        label = QtGui.QLabel('Cantidad de Personas')
        h_layout = QtGui.QHBoxLayout()
        h_layout.addWidget(label)
        button_subir = QtGui.QPushButton('Subir Persona')
        button_bajar = QtGui.QPushButton('Bajar Persona')
        h_layout.addWidget(button_subir)
        h_layout.addWidget(button_bajar)
        h_layout.addWidget(label)

        button_subir.clicked.connect(self.controlador.handler_subir_persona)

        self.setLayout(h_layout)
        self.setWindowTitle('Proyecto del Auto')
        self.Geometry(200,200,200,200)
        self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
