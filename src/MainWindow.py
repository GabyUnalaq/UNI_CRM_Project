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

from src.EmailWindow import EmailWindow
from src.EntryWindow import EntryWindow
from data.config import read_data_base


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
        self.Qbutton_general_comp = self.findChild(QPushButton, "Qbutton_general_comp")
        self.Qbutton_general_1 = self.findChild(QPushButton, "Qbutton_general_1")
        self.Qbutton_general_2 = self.findChild(QPushButton, "Qbutton_general_2")

        self.Qbox_client = self.findChild(QGroupBox, "Qbox_client")
        self.Qbutton_client_add = self.findChild(QPushButton, "Qbutton_client_add")
        self.Qbutton_client_modif = self.findChild(QPushButton, "Qbutton_client_modif")
        self.Qbutton_client_del = self.findChild(QPushButton, "Qbutton_client_del")
        self.Qbutton_client_1 = self.findChild(QPushButton, "Qbutton_client_1")
        self.Qbutton_client_2 = self.findChild(QPushButton, "Qbutton_client_2")

        # Members
        self.EmailWindow = EmailWindow()
        self.EntryWindow = EntryWindow()

        self.data_base = read_data_base()

        # Signals
        self.Qbutton_general_email.clicked.connect(self.clicked_email_window)

        self.Qbutton_client_add.clicked.connect(self.clicked_add_entry)
        self.Qbutton_client_modif.clicked.connect(self.clicked_modif_entry)
        self.Qbutton_client_del.clicked.connect(self.clicked_del_entry)

        # Init
        # TODO:

    # Initialization ---------------------------------------------------------------------------------------------------
    # TODO:

    # Methods ----------------------------------------------------------------------------------------------------------
    def closeEvent(self, event):
        exit_result = QMessageBox.question(self, "Inchidere..",
                                           "Doriti sa inchideti CRM-ul?",
                                           QMessageBox.Yes | QMessageBox.No)
        if exit_result == QMessageBox.Yes:
            event.accept()
        elif exit_result == QMessageBox.No:
            event.ignore()

    # Slots ------------------------------------------------------------------------------------------------------------
        # General
    def clicked_email_window(self):
        self.EmailWindow.show()
        self.hide()

        # Client
    def clicked_add_entry(self):
        self.EntryWindow.saved.connect(self.saved_entry)
        self.EntryWindow.show()

    def clicked_modif_entry(self):
        self.EntryWindow.set_data("Ananas")
        self.EntryWindow.saved.connect(self.saved_entry)
        self.EntryWindow.show()

    def clicked_del_entry(self):
        # TODO
        pass

    @pyqtSlot()
    def saved_entry(self):
        entry = self.EntryWindow.get_data()
        print(entry)


def show_window():
    app = QApplication([])
    window = CRMMainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
