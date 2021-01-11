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
import data.config as config

# Tree: https://www.youtube.com/watch?v=dqg0L7Qw3ko
# Table: https://www.youtube.com/watch?v=xL2NdSubiNY
# Table2: https://www.youtube.com/watch?v=l2OoXj1Z2hM


class CRMMainWindow(QMainWindow, config.Config):
    def __init__(self, parent=None):
        super(CRMMainWindow, self).__init__(parent)
        uic.loadUi(r"..\ui\MainInterface.ui", self)
        self.setWindowTitle("CRM by the Joestars")

        # Widgets
        self.Qmain_window = self.findChild(QWidget, "Qmain_window")

        self.Qtable = self.findChild(QTableWidget, "Qtable")
        self.Qtext_search = self.findChild(QLineEdit, "Qtext_search")
        self.Qlist_category = self.findChild(QTreeWidget, "Qlist_category")

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

        self.data_base = self.read_data_base()

        # Signals
        self.Qtable.cellClicked.connect(self.clicked_cell)
        self.Qlist_category.itemClicked.connect(self.clicked_category)

        self.Qbutton_general_email.clicked.connect(self.clicked_email_window)

        self.Qbutton_client_add.clicked.connect(self.clicked_add_entry)
        self.Qbutton_client_modif.clicked.connect(self.clicked_modif_entry)
        self.Qbutton_client_del.clicked.connect(self.clicked_del_entry)

        # Init
        self.init_data_base()

    # Initialization ---------------------------------------------------------------------------------------------------
    def init_data_base(self):
        # self.setCentralWidget(self.Qtable)
        # self.Qtable.fitInView(Qt.KeepAspectRatio)

        self.Qtable.setColumnCount(len(self.CRITERIA))
        self.Qtable.setRowCount(len(self.data_base['entries']))
        self.Qtable.setHorizontalHeaderLabels(self.CRITERIA)

        # Load data
        for row in range(0, len(self.data_base['entries'])):
            for col in range(0, len(self.CRITERIA)):
                item = self.data_base['entries'][row][list(self.data_base['entries'][row])[col]]
                self.Qtable.setItem(row, col, QTableWidgetItem(item))

        self.Qtable.resizeColumnsToContents()
        self.Qtable.resizeRowsToContents()

    # Methods ----------------------------------------------------------------------------------------------------------
    def closeEvent(self, event):
        exit_result = QMessageBox.question(self, "Inchidere..",
                                           "Doriti sa inchideti CRM-ul?",
                                           QMessageBox.Yes | QMessageBox.No)
        if exit_result == QMessageBox.Yes:
            event.accept()
        elif exit_result == QMessageBox.No:
            event.ignore()

    def refresh_data_base(self):
        self.Qtable.setRowCount(len(self.data_base['entries']))

        # Load data
        for row in range(0, len(self.data_base['entries'])):
            for col in range(0, len(self.CRITERIA)):
                item = self.data_base['entries'][row][list(self.data_base['entries'][row])[col]]
                self.Qtable.setItem(row, col, QTableWidgetItem(item))

        self.Qtable.resizeColumnsToContents()
        self.Qtable.resizeRowsToContents()

    # Slots ------------------------------------------------------------------------------------------------------------
    def clicked_category(self):
        item = "Da, desigur, inspiratie"
        print(item)
        # TODO

    def clicked_cell(self, row, col):
        print(self.data_base['entries'][row][list(self.data_base['entries'][row])[col]])

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
