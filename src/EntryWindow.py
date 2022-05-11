"""
    CRM Entry Window
    Used for adding / modifying an entry
    Author: Gabriel Tomuta
"""

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import re

'''
Access an item:
    self.data_base["entries"][0]["name_f"] = "Siemens"
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
        self.Qtext_obs = self.findChild(QPlainTextEdit, "Qtext_obs")  # Observatii
        self.Qtext_error = self.findChild(QPlainTextEdit, "Qtext_error")
        self.Qtext_act = self.findChild(QPlainTextEdit, "Qtext_act")
        self.Qtext_reminder = self.findChild(QPlainTextEdit, "Qtext_reminder")

        self.Qtext_name_p = self.findChild(QLineEdit, "Qtext_name_p")  # nume + prenume
        self.Qtext_dates = self.findChild(QLineEdit, "Qtext_dates")    # date de contact pers
        self.Qtext_name_f = self.findChild(QLineEdit, "Qtext_name_f")  # nume companie
        self.Qtext_cui = self.findChild(QLineEdit, "Qtext_cui")        # CUI
        self.Qtext_email = self.findChild(QLineEdit, "Qtext_email")    # email companie
        self.Qtext_tel = self.findChild(QLineEdit, "Qtext_tel")        # telefon companie
        self.Qtext_num_a = self.findChild(QLineEdit, "Qtext_num_a")    # numar angajati
        self.Qtext_caen = self.findChild(QLineEdit, "Qtext_caen")      # Cod CAEN
        self.Qtext_fund = self.findChild(QLineEdit, "Qtext_fund")      # Ce se doreste a fi finantat

        # Members
        self.data = None

        # Signals
        self.Qbutton_save.clicked.connect(self.on_click_save)
        self.Qbutton_abort.clicked.connect(self.close)

    # Methods ----------------------------------------------------------------------------------------------------------
    def error_check(self):
        # TODO check
        if self.Qtext_name_p.text() == "":
            self.Qtext_error.setPlainText("Introduceti numele persoanei de contact.")
            return True
        if self.Qtext_name_f.text() == "":
            self.Qtext_error.setPlainText("Introduceti numele firmei.")
            return True
        if self.Qtext_cui.text() == "":
            self.Qtext_error.setPlainText("Introduceti codul CUI al firmei.")
            return True
        if self.Qtext_cui.text() != "" and not any(ch in '0123456789' for ch in self.Qtext_cui.text()):
            self.Qtext_error.setPlainText("CUI invalid.")
            return True
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if self.Qtext_email.text() != "" and not re.fullmatch(email_regex, self.Qtext_email.text()):
            self.Qtext_error.setPlainText("Email invalid.")
            return True
        if self.Qtext_tel.text() == "":
            self.Qtext_error.setPlainText("Introduceti un nr. de telefon al firmei.")
            return True
        if self.Qtext_tel.text() != "" and not any(ch in ' .0123456789' for ch in self.Qtext_tel.text()):
            self.Qtext_error.setPlainText("Numar de telefon invalid.")
            return True
        if self.Qtext_num_a.text() != "" and not any(ch in '0123456789' for ch in self.Qtext_num_a.text()):
            self.Qtext_error.setPlainText("Numar de angajati invalid.")
            return True
        if self.Qtext_caen.text() == "":
            self.Qtext_error.setPlainText("Introduceti codul CAEN al firmei.")
            return True
        if self.Qtext_caen.text() != "" and not any(ch in '0123456789' for ch in self.Qtext_caen.text()):
            self.Qtext_error.setPlainText("Cod CAEN invalid.")
            return True
        if self.Qtext_fund.text() == "":
            self.Qtext_error.setPlainText("Introduceti finantarea.")
            return True
        return False

    def set_data(self, data):
        self.Qtext_error.setPlainText('')
        self.Qtext_name_p.setText(str(data["name_p"]))
        self.Qtext_dates.setText(str(data["dates"]))
        self.Qtext_name_f.setText(str(data["name_f"]))
        self.Qtext_cui.setText(str(data["cui"]))
        self.Qtext_email.setText(str(data["email"]))
        self.Qtext_tel.setText(str(data["tel"]))
        self.Qtext_num_a.setText(str(data["num_a"]))
        self.Qtext_caen.setText(str(data["caen"]))
        self.Qtext_fund.setText(str(data["fund"]))
        self.Qtext_obs.setPlainText(str(data["obs"]))

    def set_empty(self):
        self.Qtext_error.setPlainText('')
        self.Qtext_name_p.setText('')
        self.Qtext_dates.setText('')
        self.Qtext_name_f.setText('')
        self.Qtext_cui.setText('')
        self.Qtext_email.setText('')
        self.Qtext_tel.setText('')
        self.Qtext_num_a.setText('')
        self.Qtext_caen.setText('')
        self.Qtext_fund.setText('')
        self.Qtext_obs.setPlainText('')

    def get_data(self):
        self.data = {
            "name_p": self.Qtext_name_p.text(),
            "dates": self.Qtext_dates.text(),
            "name_f": self.Qtext_name_f.text(),
            "cui": self.Qtext_cui.text(),
            "email": self.Qtext_email.text(),
            "tel": self.Qtext_tel.text(),
            "num_a": self.Qtext_num_a.text(),
            "caen": self.Qtext_caen.text(),
            "fund": self.Qtext_fund.text(),
            "obs": self.Qtext_obs.toPlainText()
        }
        if not self.error_check():
            return self.data
        else:
            pass

    # Slots ------------------------------------------------------------------------------------------------------------
    def on_click_save(self):
        self.Qtext_error.setPlainText('')
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
