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
        self.csv = None
        uic.loadUi(r"..\ui\LoginInterface.ui", self)
        self.setWindowTitle("Login into CRM")

        # Widgets
        self.Qmain_login = self.findChild(QWidget, "Qmain_login")
        self.Qbutton_login = self.findChild(QPushButton, "Qbutton_login")
        self.Qbutton_login.setCheckable(True)
        self.Qtext_email = self.findChild(QLineEdit, "Qtext_email")
        self.Qtext_password = self.findChild(QLineEdit, "Qtext_password")

        self.Qtext_email.setPlaceholderText('Introduceti e-mail')
        self.Qtext_password.setPlaceholderText('Introduceti parola')
        self.Qtext_password.setEchoMode(QLineEdit.Password)

        # Members
        # TODO:

        # Signals
        self.Qbutton_login.clicked.connect(self.check_password)
        # TODO: Horsexiu

        # Init
        # TODO:

    def initialization(self):
        self.read_csv()
        print(self.csv)
        # TODO

    # Methods ----------------------------------------------------------------------------------------------------------
    # TODO:

    # Slots ------------------------------------------------------------------------------------------------------------
    # TODO:

    def read_csv(self):
        with open('../data/login_info.csv') as csv_file:
            self.csv = csv.reader(csv_file, delimiter=',')

    def check_password(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        if self.Qtext_email.text() == 'Farkas' and self.Qtext_password.text() == 'prost34':
            msg.setWindowTitle("Locare reusita")
            msg.setText('Success')
            msg.exec_()
            self.redirect_to_main()
            app.quit()
        else:
            msg.setWindowTitle("Eroare")
            msg.setText('E-mail sau parola incorecta')
            msg.exec_()

    def redirect_to_main(self):
        pass
        # TODO


def show_window():
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
