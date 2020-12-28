"""
    CRM Main Window
    Authors: Rares Horju, Gabriel Tomuta
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import time
import threading
import csv


class CRMMain(QMainWindow):
    def __init__(self, parent=None):
        super(CRMMain, self).__init__(parent)
        uic.loadUi(r"..\ui\MainInterface.ui", self)
        self.setWindowTitle("CRM by the Joestars")

        # Widgets
        self.Qmain_window = self.findChild(QWidget, "Qmain_window")

        self.Qtable = self.findChild(QColumnView, "Qtable")
        self.Qtext_search = self.findChild(QTextEdit, "Qtext_search")
        self.Qlist_category = self.findChild(QListView, "Qlist_category")
        self.Qvert_scroll_bar = self.findChild(QScrollBar, "Qvert_scroll_bar")

        self.Qbox_general = self.findChild(QGroupBox, "Qbox_general")
        self.Qbutton_general_1 = self.findChild(QPushButton, "Qbutton_general_1")
        self.Qbutton_general_2 = self.findChild(QPushButton, "Qbutton_general_2")

        self.Qbox_client = self.findChild(QGroupBox, "Qbox_client")
        self.Qbutton_client_1 = self.findChild(QPushButton, "Qbutton_client_1")
        self.Qbutton_client_2 = self.findChild(QPushButton, "Qbutton_client_2")

        # Members
        # TODO:

        # Signals
        # TODO:

        # Init
        # TODO:

    # Initialization ---------------------------------------------------------------------------------------------------
    # TODO:

    # Methods ----------------------------------------------------------------------------------------------------------
    # TODO:

    # Slots ------------------------------------------------------------------------------------------------------------
    # TODO:


def show_window():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
