"""
    CRM Action Window
    NOT FUNCTIONAL
    Authors: Gabriel Tomuta
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import time
import threading


class ActionWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"..\ui\ActionInterface.ui", self)
        self.setWindowTitle("Actiuni")

        # Widgets
        self.Qbutton_actions = self.findChild(QPushButton, "Qbutton_actions")
        self.Qbutton_reminder = self.findChild(QPushButton, "Qbutton_reminder")
        self.Qtext_obs = self.findChild(QPlainTextEdit, "Qtext_obs")
        self.Qtext_data = self.findChild(QPlainTextEdit, "Qtext_data")

        # Members
        # TODO

        # Signals
        self.Qbutton_actions.clicked.connect(self.on_click_act)
        # TODO

        # Init
        # TODO

    # Initialization ---------------------------------------------------------------------------------------------------
    # TODO:

    # Methods ----------------------------------------------------------------------------------------------------------
    # TODO:

    # Slots ------------------------------------------------------------------------------------------------------------
    def on_click_act(self):
        print("Sa apasat butonul de actiuni")
        # TODO


def show_window():
    app = QApplication([])
    window = ActionWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
