"""
    CRM Email Window
    NOT FUNCTIONAL
    Authors: Gabriel Tomuta, Patrania Bogdan
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import time
import threading


class ReportWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"..\ui\ReportInterface.ui", self)
        self.setWindowTitle("Rapoarte")

        # Widgets
        self.Qbutton_send = self.findChild(QPushButton, "Qbutton_send")
        self.Qbutton_abort = self.findChild(QPushButton, "Qbutton_abort")
        self.Qlist_format = self.findChild(QListWidget, "Qlist_format")
        self.Qlist_main = self.findChild(QListWidget, "Qlist_main")

        # Members
        self.data_base = None
        self.format = None
        self.cat_clicked = []

        # Signals
        self.Qbutton_send.clicked.connect(self.on_clicked_button_send)
        self.Qbutton_abort.clicked.connect(self.close)

        self.Qlist_format.itemClicked.connect(self.on_format_clicked)
        self.Qlist_main.itemClicked.connect(self.on_list_clicked)

        # Init
        self.init_lists()

    # Initialization ---------------------------------------------------------------------------------------------------
    def init_lists(self):
        """
        This method creates the list members from self.data_base['criteria']
        It updates BOTH the lists
        """
        # TODO function
        pass

    # Methods ----------------------------------------------------------------------------------------------------------
    def update_data_base(self, data_base):
        self.data_base = data_base

    # Slots ------------------------------------------------------------------------------------------------------------
    def on_clicked_button_send(self):
        print('S-a apasat pe butonul de trimitere')
        # TODO send report
        self.hide()

    def on_format_clicked(self):
        print('S-a apasat un membru din lista')
        # TODO if clicked

    def on_list_clicked(self):
        print('Sa apasat un item din lista mare')
        # TODO if clicked


def show_window():
    app = QApplication([])
    window = ReportWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
