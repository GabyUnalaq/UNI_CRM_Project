"""
    CRM Email Window
    Authors: Gabriel Tomuta, Patrania Bogdan
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import time
import threading
import csv


class EmailWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"..\ui\EmailInterface.ui", self)
        self.setWindowTitle("Send E-mail")

        # Widgets
        self.Qmain_email = self.findChild(QWidget, "Qmain_email")
        self.Qcontent_attachments = self.findChild(QWidget, "Qcontent_attachments")

        self.Qtext_message = self.findChild(QPlainTextEdit, "Qtext_message")
        self.Qtext_subject = self.findChild(QTextEdit, "Qtext_subject")
        self.Qtext_to = self.findChild(QTextEdit, "Qtext_to")

        self.Qbutton_send = self.findChild(QPushButton, "Qbutton_send")
        self.Qbutton_save = self.findChild(QPushButton, "Qbutton_save")
        self.Qbutton_attach = self.findChild(QPushButton, "Qbutton_attach")
        self.Qbutton_abort = self.findChild(QPushButton, "Qbutton_abort")

        self.Qcheck_bold = self.findChild(QCheckBox, "Qcheck_bold")
        self.Qcheck_italic = self.findChild(QCheckBox, "Qcheck_italic")
        self.Qcheck_underline = self.findChild(QCheckBox, "Qcheck_underline")
        self.Qcheck_strikeout = self.findChild(QCheckBox, "Qcheck_strikout")

        self.Qcheck_arial = self.findChild(QCheckBox, "Qcheck_arial")
        self.Qcheck_calibri = self.findChild(QCheckBox, "Qcheck_calibri")
        self.Qcheck_courier = self.findChild(QCheckBox, "Qcheck_courier")
        self.Qcheck_tnr = self.findChild(QCheckBox, "Qcheck_tnr") 

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
    window = EmailWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
