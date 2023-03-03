from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QDialog
from PySide6.QtCore import QPoint
import sqlite3
import UI
import database_setup


class UpdateEntriesWindow(QtWidgets.QWidget):
    def __init__(self, conn: sqlite3.Connection, cur: sqlite3.Cursor):
        super().__init__()

        width, height = self.screen().size().toTuple()
        screen_center = QPoint(width/2, height/2)
        self.move(screen_center)

        self.prompt = QLabel("What would you like to do?")

        self.update_button = QPushButton("Update Entries")
        self.proceed_button = QPushButton("View Existing Entries")

        self.connection = conn
        self.cursor = cur

        self.main_window = UI.Window(self.connection, self.cursor)

        self.create_window()

    def create_window(self):
        self.setWindowTitle("Update Submission Records?")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.proceed_button)

        self.update_button.clicked.connect(self.update_button_clicked)
        self.proceed_button.clicked.connect(self.proceed_button_pressed)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.prompt)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def update_button_clicked(self):
        response = database_setup.get_from_api()
        database_setup.write_response_to_database(response, self.cursor)
        self.connection.commit()

        confirm_layout = QVBoxLayout()
        confirm_box = QDialog(self)
        ok_button = QPushButton("Close")
        confirm_message = QLabel("Database Updated")
        confirm_layout.addWidget(confirm_message)
        confirm_layout.addWidget(ok_button)
        confirm_box.setLayout(confirm_layout)
        ok_button.clicked.connect(confirm_box.close)
        confirm_box.exec()

    def proceed_button_pressed(self):
        self.main_window.show()
        self.hide()
