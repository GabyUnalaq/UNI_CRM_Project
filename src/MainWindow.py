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

from src.EmailWindow import EmailWindow
from src.ClientAddWindow import ClientAddWindow


class CRMMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(CRMMainWindow, self).__init__(parent)
        uic.loadUi(r"..\ui\MainInterface.ui", self)
        self.setWindowTitle("CRM by the Joestars")

        # Widgets
        self.Qmain_window = self.findChild(QWidget, "Qmain_window")

        self.Qtable = self.findChild(QColumnView, "Qtable")
        self.Qtext_search = self.findChild(QTextEdit, "Qtext_search")
        self.Qlist_category = self.findChild(QListView, "Qlist_category")
        self.Qvert_scroll_bar = self.findChild(QScrollBar, "Qvert_scroll_bar")

        self.Qbox_general = self.findChild(QGroupBox, "Qbox_general")
        self.Qbutton_general_email = self.findChild(QPushButton, "Qbutton_general_email")
        self.Qbutton_general_1 = self.findChild(QPushButton, "Qbutton_general_1")
        self.Qbutton_general_2 = self.findChild(QPushButton, "Qbutton_general_2")

        self.Qbox_client = self.findChild(QGroupBox, "Qbox_client")
        self.Qbutton_client_add = self.findChild(QPushButton, "Qbutton_client_add")
        self.Qbutton_client_del = self.findChild(QPushButton, "Qbutton_client_del")
        self.Qbutton_client_1 = self.findChild(QPushButton, "Qbutton_client_1")
        self.Qbutton_client_2 = self.findChild(QPushButton, "Qbutton_client_2")

        # Members
        self.EmailWindow = EmailWindow()
        self.ClientAddWindow = ClientAddWindow()

        # Signals
        self.Qbutton_general_email.clicked.connect(self.open_email_window)
        self.Qbutton_client_add.clicked.connect(self.open_client_add_window)

        # Init
        # TODO:

    # Initialization ---------------------------------------------------------------------------------------------------
    # TODO:

    # Methods ----------------------------------------------------------------------------------------------------------
    # TODO:

    # Slots ------------------------------------------------------------------------------------------------------------
    def open_email_window(self):
        self.EmailWindow.show()
        self.hide()

    def open_client_add_window(self):
        self.ClientAddWindow.show()


def show_window():
    app = QApplication([])
    window = CRMMainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
