# -*- coding: utf-8 -*-
import sys
sys.path.append('../Modelos')
from auto import *

class MainControlador():

    def __init__(self, una_ventana):
        self.auto = Auto()
        self.ventana = una_ventana

    def handler_subir_persona(self):
        self.auto.subir_persona()
        self.actualizar_label()
        #print self.auto.cantidad_personas

    def handler_bajar_persona(self):
        self.auto.bajar_persona()
        self.actualizar_label()
        #print self.auto.cantidad_personas

    def handler_bajar_persona5(self):
        i = 1
        while i <= 5:
            i += 1
            self.handler_bajar_persona()

    def actualizar_label(self):
        self.ventana.label.setText(str(self.auto.cantidad_personas))
