"""
    CRM Interface
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Facultate\Proiect PA\ui\MainInterface.ui", self)
        self.setWindowTitle("CRM by the Joestars")

        # Widgets
        self.qtCRMInterface = self.findChild(QWidget, "qtCRMInterface")
        self.qtClientActions = self.findChild(QGroupBox, "qtClientActions")
        self.pushButton = self.findChild(QPushButton, "pushButton")
        self.pushButton_2 = self.findChild(QPushButton, "pushButton_2")
        self.pushButton_3 = self.findChild(QPushButton, "pushButton_3")
        self.pushButton_4 = self.findChild(QPushButton, "pushButton_4")
        self.listView = self.findChild(QListView, "listView")
        self.qtDetaliiClient = self.findChild(QColumnView, "qtDetaliiClient")
        self.textEdit = self.findChild(QTextEdit, "textEdit")
        self.verticalScrollBar = self.findChild(QScrollBar, "verticalScrollBar")

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
