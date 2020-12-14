"""
    CRM Login Window
    Authors: Gabriel Tomuta
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import time
import threading
import csv


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"..\ui\LoginInterface.ui", self)
        self.setWindowTitle("Send E-mail")

        # Widgets
        self.Qmain_login = self.findChild(QWidget, "Qmain_login")
        self.Qbutton_login = self.findChild(QPushButton, "Qbutton_login")
        self.Qtext_email = self.findChild(QPlainTextEdit, "Qtext_email")
        self.Qtext_password = self.findChild(QPlainTextEdit, "Qtext_password")

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
    window = LoginWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
