"""
    CRM Add Entry Window
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


# TODO
# Size failing to work properly


class ClientAddWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"..\ui\ClientAddInterface.ui", self)
        self.setWindowTitle("Adaugare intrare")

        # Widgets
        self.Qbutton_save = self.findChild(QPushButton, "Qbutton_save")
        self.Qbutton_abort = self.findChild(QPushButton, "Qbutton_abort")
        self.Qtext_obs = self.findChild(QPlainTextEdit, "Qtext_obs")
        self.Qtext_error = self.findChild(QPlainTextEdit, "Qtext_error")

        self.Qtext_name_p = self.findChild(QPlainTextEdit, "Qtext_name_p")
        self.Qtext_dates = self.findChild(QPlainTextEdit, "Qtext_dates")
        self.Qtext_name_f = self.findChild(QPlainTextEdit, "Qtext_name_f")
        self.Qtext_cui = self.findChild(QPlainTextEdit, "Qtext_cui")
        self.Qtext_email = self.findChild(QPlainTextEdit, "Qtext_email")
        self.Qtext_tel = self.findChild(QPlainTextEdit, "Qtext_tel")
        self.Qtext_num_a = self.findChild(QPlainTextEdit, "Qtext_num_a")
        self.Qtext_num_a = self.findChild(QPlainTextEdit, "Qtext_num_a")
        self.Qtext_fund = self.findChild(QPlainTextEdit, "Qtext_fund")

        # Members
        # TODO:

        # Signals
        self.Qbutton_save.clicked.connect(self.click_save)
        self.Qbutton_abort.clicked.connect(self.click_abort)

        # Init
        # TODO:

    # Initialization ---------------------------------------------------------------------------------------------------
    # TODO:

    # Methods ----------------------------------------------------------------------------------------------------------
    # TODO:

    # Slots ------------------------------------------------------------------------------------------------------------
    def click_save(self):
        pass
        # TODO

    def click_abort(self):
        pass
        # TODO


def show_window():
    app = QApplication([])
    window = ClientAddWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
