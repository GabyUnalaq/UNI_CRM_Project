"""
    CRM Login Window
    Authors: Gabriel Tomuta, Rares Horju
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import time
import threading

from src.MainWindow import CRMMainWindow
from data.config import check_in_csv


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
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
        self.MainWindow = CRMMainWindow(self)

        # Signals
        self.Qbutton_login.clicked.connect(self.check_password)

        # Init

    # Methods ----------------------------------------------------------------------------------------------------------
    def redirect_to_main(self):
        self.MainWindow.show()
        self.hide()

    # Slots ------------------------------------------------------------------------------------------------------------
    def check_password(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        if check_in_csv(self.Qtext_email.text(), self.Qtext_password.text()) is True:
            msg.setWindowTitle("Locare reusita")
            msg.setText('Success')
            msg.exec_()
            self.redirect_to_main()
            # app.quit()
        else:
            msg.setWindowTitle("Eroare")
            msg.setText('E-mail sau parola incorecta')
            msg.exec_()


def show_window():
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
