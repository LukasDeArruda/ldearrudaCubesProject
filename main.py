import sqlite3
import sys
from requests.auth import HTTPBasicAuth
import requests
import json
from secrets import api_key
import database_setup
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QDialog, QDialogButtonBox
from PySide6.QtCore import QPoint, QCoreApplication
import UI


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
        response = get_from_api()
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


def get_from_api():
    url = 'https://lukasdearruda.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries.json'
    entry = requests.get(url, auth=HTTPBasicAuth(api_key, 'pass'))
    if entry.status_code != 200:
        print(f"Failed to get data, response code: {entry.status_code} and error message: {entry.reason}")
        sys.exit(-1)
    json_response = entry.json()
    return json_response


def write_response_to_file(response):
    file = open("responses.json", "w+")
    file.write(str(json.dumps(response, indent=4)))
    file.close()


def main():
    connection, cursor = database_setup.open_db("responses.db")
    database_setup.create_table(cursor)
    connection.commit()

    app = QtWidgets.QApplication()
    update_window = UpdateEntriesWindow(connection, cursor)
    update_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
