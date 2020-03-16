# -*- Coding: UTF-8 -*-
# Programa: BAndeja de mensajes
# objetivo: Su funcion es recibir, notificar y revidsar los mensajes.
# Autor: Luis Enrique Consuegra
# Fecha: 15/03/2020

import sys
import plataform
import os

class Mensajeria(self):
    """Recibira los mensajes y notificara al usuario""""
    def __init__(self):
        self.mensajes =list()

        self.Opciones = {"1": self.add_Mensaje,
                         "2": self.notificar_mensaje,
                         "3": self.mensaje_sin_leer,
                         "4": self.Ver_mensaje,
                         "5": self.borrar_mensaje,
                         "6": self.salir}

    def menu(self):
