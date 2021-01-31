"""
    CRM Entry Window
    Used for adding / modifying an entry
    Author: Gabriel Tomuta
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import time
import threading

# TODO Read FArky
'''
ca sa accesezi un item din baza de date:
self.data_base["entries"][0]["name_p"] = "Bita Robert"
'''


class EntryWindow(QWidget):
    entrySavedSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        uic.loadUi(r"..\ui\EntryInterface.ui", self)
        self.setWindowTitle("Entry Interface")

        # Widgets
        self.Qbutton_save = self.findChild(QPushButton, "Qbutton_save")
        self.Qbutton_abort = self.findChild(QPushButton, "Qbutton_abort")
        self.Qtext_obs = self.findChild(QPlainTextEdit, "Qtext_obs")
        self.Qtext_error = self.findChild(QPlainTextEdit, "Qtext_error")
        self.Qtext_act = self.findChild(QPlainTextEdit, "Qtext_act")
        self.Qtext_reminder = self.findChild(QPlainTextEdit, "Qtext_reminder")

        self.Qtext_name_p = self.findChild(QLineEdit, "Qtext_name_p")
        self.Qtext_dates = self.findChild(QLineEdit, "Qtext_dates")
        self.Qtext_name_f = self.findChild(QLineEdit, "Qtext_name_f")
        self.Qtext_cui = self.findChild(QLineEdit, "Qtext_cui")
        self.Qtext_email = self.findChild(QLineEdit, "Qtext_email")
        self.Qtext_tel = self.findChild(QLineEdit, "Qtext_tel")
        self.Qtext_num_a = self.findChild(QLineEdit, "Qtext_num_a")
        self.Qtext_caen = self.findChild(QLineEdit, "Qtext_caen")
        self.Qtext_fund = self.findChild(QLineEdit, "Qtext_fund")

        # Members
        self.data = None

        # Signals
        self.Qbutton_save.clicked.connect(self.on_click_save)
        self.Qbutton_abort.clicked.connect(self.close)

        # Init
        # TODO

    # Initialization ---------------------------------------------------------------------------------------------------
    # TODO:

    # Methods ----------------------------------------------------------------------------------------------------------
    def error_check(self):
        if self.Qtext_name_p.text() is "":
            self.Qtext_error.setPlainText("Introduceti numele persoanei de contact.")
            return True
        if self.Qtext_dates.text() is "":
            self.Qtext_error.setPlainText("Introduceti datele persoanei de contact.")
            return True
        if self.Qtext_name_f.text() is "":
            self.Qtext_error.setPlainText("Introduceti numele firmei.")
            return True
        # TODO Farky
        return False

    def set_data(self, data):
        # self.data = data
        self.Qtext_name_p.setText(str(data["name_p"]))
        self.Qtext_dates.setText(str(data["dates"]))
        self.Qtext_name_f.setText(str(data["name_f"]))
        # TODO Farky

    def set_empty(self):
        self.Qtext_name_p.setText('')
        self.Qtext_dates.setText('')
        self.Qtext_name_f.setText('')
        # TODO Farky

    def get_data(self):
        name = self.Qtext_name_p.text()
        info = self.Qtext_dates.text()
        company = self.Qtext_name_f.text()
        # TODO Farky
        data_2_send = {
            "name_p": name,
            "dates": info,
            "name_f": company
            # TODO Farky
        }
        self.data = data_2_send
        if name is not "" or info is not "" or company is not "":
            return self.data
        else:
            pass

    # Slots ------------------------------------------------------------------------------------------------------------
    def on_click_save(self):
        if not self.error_check():
            self.entrySavedSignal.emit()
            self.close()


def show_window():
    app = QApplication([])
    window = EntryWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
