"""
    CRM Main Window
    Authors: Rares Horju, Gabriel Tomuta
"""

from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import time
import threading

from src.EmailWindow import EmailWindow
from src.EntryWindow import EntryWindow
from src.LoginWindow import LoginWindow
import data.config as config

# Tree: https://www.youtube.com/watch?v=dqg0L7Qw3ko
# Table: https://www.youtube.com/watch?v=xL2NdSubiNY
# Table2: https://www.youtube.com/watch?v=l2OoXj1Z2hM


class CRMMainWindow(QWidget, config.Config):
    def __init__(self, parent=None):
        super(CRMMainWindow, self).__init__(parent)
        uic.loadUi(r"..\ui\MainInterface.ui", self)
        self.setWindowTitle("CRM by the Joestars")

        # Widgets
        self.Qtable = self.findChild(QTableView, "Qtable")
        self.Qtext_search = self.findChild(QLineEdit, "Qtext_search")
        self.Qbutton_search = self.findChild(QPushButton, "Qbutton_search")  # Search

        self.Qbutton_general_email = self.findChild(QPushButton, "Qbutton_general_email")  # Email
        self.Qbutton_general_notif = self.findChild(QPushButton, "Qbutton_general_notif")  # Notificari
        self.Qbutton_general_lich = self.findChild(QPushButton, "Qbutton_general_lich")  # Licitatii
        self.Qbutton_general_rap = self.findChild(QPushButton, "Qbutton_general_rap")  # Rapoarte

        self.Qbutton_client_add = self.findChild(QPushButton, "Qbutton_client_add")  # Adauga intrare
        self.Qbutton_client_modif = self.findChild(QPushButton, "Qbutton_client_modif")  # Modifica intrare
        self.Qbutton_client_del = self.findChild(QPushButton, "Qbutton_client_del")  # Sterge intrare
        self.Qbutton_client_comp = self.findChild(QPushButton, "Qbutton_client_comp")  # Info companie

        # Members
        self.LoginWindow = LoginWindow()
        self.EmailWindow = EmailWindow()
        self.EntryWindow = EntryWindow()

        self.data_base = self.read_data_base()

        # Signals
        self.LoginWindow.loginSuccessSignal.connect(self.on_show)
        self.EntryWindow.entrySavedSignal.connect(self.saved_entry)
        self.Qtable.cellClicked.connect(self.on_clicked_cell)

        self.Qbutton_general_email.clicked.connect(self.on_clicked_email_window)
        self.Qbutton_client_add.clicked.connect(self.on_clicked_add_entry)
        self.Qbutton_client_modif.clicked.connect(self.on_clicked_modif_entry)
        self.Qbutton_client_del.clicked.connect(self.on_clicked_del_entry)

        # Init
        self.LoginWindow.show()
        self.init_data_base()

    # Initialization ---------------------------------------------------------------------------------------------------
    def init_data_base(self):
        self.Qtable.setColumnCount(len(self.data_base['criteria']))
        self.Qtable.setRowCount(len(self.data_base['entries']))
        self.Qtable.setHorizontalHeaderLabels(self.data_base['criteria'])

        # Load data
        for row in range(0, len(self.data_base['entries'])):
            for col in range(0, len(self.data_base['criteria'])):
                item = self.data_base['entries'][row][list(self.data_base['entries'][row])[col]]
                self.Qtable.setItem(row, col, QTableWidgetItem(item))

        self.Qtable.resizeColumnsToContents()
        self.Qtable.resizeRowsToContents()

    # Events -----------------------------------------------------------------------------------------------------------
    def closeEvent(self, event):
        exit_result = QMessageBox.question(self, "Inchidere..",
                                           "Doriti sa inchideti CRM-ul?",
                                           QMessageBox.Yes | QMessageBox.No)
        if exit_result == QMessageBox.Yes:
            event.accept()
        elif exit_result == QMessageBox.No:
            event.ignore()

    # Methods ----------------------------------------------------------------------------------------------------------
    def refresh_data_base(self):
        self.Qtable.setRowCount(len(self.data_base['entries']))

        # Load data
        for row in range(0, len(self.data_base['entries'])):
            for col in range(0, len(self.data_base['criteria'])):
                item = self.data_base['entries'][row][list(self.data_base['entries'][row])[col]]
                self.Qtable.setItem(row, col, QTableWidgetItem(item))

        self.Qtable.resizeColumnsToContents()
        self.Qtable.resizeRowsToContents()

    # Slots ------------------------------------------------------------------------------------------------------------
    @pyqtSlot()
    def on_show(self):
        self.LoginWindow.hide()
        self.show()

    def on_clicked_cell(self, row, col):
        print(self.data_base['entries'][row][list(self.data_base['entries'][row])[col]])

        # General
    def on_clicked_email_window(self):
        self.EmailWindow.show()

        # Client
    def on_clicked_add_entry(self):
        self.EntryWindow.show()

    def on_clicked_modif_entry(self):
        self.EntryWindow.set_data("Ananas")
        self.EntryWindow.show()

    def on_clicked_del_entry(self):
        # TODO
        pass

    @pyqtSlot()
    def saved_entry(self):
        entry = self.EntryWindow.get_data()
        print(entry)


def show_window():
    app = QApplication([])
    window = CRMMainWindow()
    app.exec_()


if __name__ == "__main__":
    show_window()
