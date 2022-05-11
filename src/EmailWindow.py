"""
    CRM Email Window
    NOT FUNCTIONAL
    Authors: Gabriel Tomuta, Patrania Bogdan
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import time
import threading


class EmailWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"..\ui\EmailInterface.ui", self)
        self.setWindowTitle("Send E-mail")

        # Widgets
        self.Qmain_email = self.findChild(QWidget, "Qmain_email")
        self.Qcontent_attachments = self.findChild(QWidget, "Qcontent_attachments")

        self.Qtext_message = self.findChild(QTextEdit, "Qtext_message")
        self.Qtext_subject = self.findChild(QPlainTextEdit, "Qtext_subject")
        self.Qtext_to = self.findChild(QPlainTextEdit, "Qtext_to")

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

        self.Qsbox_size = self.findChild(QSpinBox, "Qsbox_size")

        # Members
        # TODO:

        # Signals
        self.Qbutton_attach.clicked.connect(self.on_clicked_button_attach)
        self.Qbutton_send.clicked.connect(self.on_clicked_button_send)
        self.Qbutton_abort.clicked.connect(self.close)

        self.Qcheck_bold.stateChanged.connect(self.on_changed_bold)

        # Init
        # self.Qtext_message.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")
        self.Qtext_message.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font> Buna ziua")

    # Initialization ---------------------------------------------------------------------------------------------------
    # TODO:

    # Methods ----------------------------------------------------------------------------------------------------------
    # TODO:

    # Slots ------------------------------------------------------------------------------------------------------------
    def on_clicked_button_send(self):
        adress = self.Qtext_to.toPlainText()
        subject = self.Qtext_subject.toPlainText()
        message = self.Qtext_message.toPlainText()
        print("Trimitem catre {0} cu titlul de {1} mesajul: {2}".format(adress, subject, message))
        self.hide()

    def on_clicked_button_attach(self):
        pass
        # TODO

    def on_changed_bold(self):
        if self.Qcheck_bold.isChecked():
            print("Vreau text bold")
        else:
            print("Nu mai vreau bold")


def show_window():
    app = QApplication([])
    window = EmailWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    show_window()
