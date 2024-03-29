from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QDialog
import sqlite3
import popup_window


class UserInfoWindow(QtWidgets.QWidget):
    def __init__(self, conn: sqlite3.Connection, cur: sqlite3.Cursor, pkey):
        super().__init__()

        self.primary_key = pkey

        self.connection = conn
        self.cursor = cur

        self.claim_button = QPushButton("Claim")
        self.cancel_button = QPushButton("Cancel")
        self.add_new_record_button = QPushButton("Add Record")

        self.email_label = QLabel("Email")
        self.email_box = QLineEdit()

        self.fname_label = QLabel("First Name")
        self.fname_box = QLineEdit()

        self.lname_label = QLabel("Last Name")
        self.lname_box = QLineEdit()

        self.title_label = QLabel("Title")
        self.title_box = QLineEdit()

        self.dept_label = QLabel("Department")
        self.dept_box = QLineEdit()

        self.submit_email = QPushButton("Enter")

        self.create_ui()

    def create_ui(self):
        self.resize(750, 250)
        self.setWindowTitle("Enter Info")

        main_layout = QVBoxLayout()

        user_info_layout = QGridLayout()

        user_info_layout.addWidget(self.email_label, 0, 0)
        user_info_layout.addWidget(self.email_box, 0, 1)

        user_info_layout.addWidget(self.submit_email, 0, 2)
        self.submit_email.clicked.connect(self.add_email_to_db)

        user_info_layout.addWidget(self.fname_label, 1, 0)
        user_info_layout.addWidget(self.fname_box, 1, 1)
        user_info_layout.addWidget(self.lname_label, 1, 2)
        user_info_layout.addWidget(self.lname_box, 1, 3)

        user_info_layout.addWidget(self.title_label, 2, 0)
        user_info_layout.addWidget(self.title_box, 2, 1)
        user_info_layout.addWidget(self.dept_label, 2, 2)
        user_info_layout.addWidget(self.dept_box, 2, 3)

        self.fname_box.setReadOnly(True)
        self.lname_box.setReadOnly(True)
        self.title_box.setReadOnly(True)
        self.dept_box.setReadOnly(True)

        button_layout = QHBoxLayout()
        self.cancel_button.clicked.connect(self.close_window)
        self.claim_button.clicked.connect(self.claim_project)
        self.add_new_record_button.clicked.connect(self.add_new_user)
        button_layout.addWidget(self.claim_button)
        button_layout.addWidget(self.add_new_record_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addStretch(1)

        main_layout.addLayout(user_info_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def add_email_to_db(self):
        # Check if email is in db, returns 1 if yes, 0 if no
        self.cursor.execute("""SELECT EXISTS(SELECT * FROM user_records 
                            WHERE claimed_email = ?)""", (self.email_box.text(),))
        is_in_db = self.cursor.fetchall()

        if is_in_db[0][0] == 1:
            self.cursor.execute("""SELECT * FROM user_records WHERE claimed_email = ?""", (self.email_box.text(),))
            selected_entry = self.cursor.fetchall()
            self.email_box.setStyleSheet("background-color: green")

            self.fname_box.setText(selected_entry[0][1])
            self.lname_box.setText(selected_entry[0][2])
            self.title_box.setText(selected_entry[0][3])
            self.dept_box.setText(selected_entry[0][4])
        else:
            popup_window_title = "Email Not Found"
            prompt_label = QLabel("Email not found. Please enter user information")
            self.email_box.setStyleSheet("background-color: red")
            popup = popup_window.PopupWindow(prompt_label, popup_window_title)
            popup.exec()
            self.fname_box.setReadOnly(False)
            self.lname_box.setReadOnly(False)
            self.title_box.setReadOnly(False)
            self.dept_box.setReadOnly(False)

        # If email is in the database, autofill the rest of the info
        # if not, prompt user to fill in the rest of their info

    def close_window(self):
        self.close()

    def claim_project(self):
        self.cursor.execute("""UPDATE responses SET claimed = 1 WHERE entryNum = ?""", (self.primary_key,))
        self.cursor.execute("""UPDATE responses SET claimed_email = ? WHERE entryNum = ?""",
                            (self.email_box.text(), self.primary_key,))
        self.connection.commit()

        popup_window_title = "Claimed"
        claimed_label = QLabel("Project claimed")
        confirmation_window = popup_window.PopupWindow(claimed_label, popup_window_title)
        confirmation_window.exec()

    def add_new_user(self):
        self.cursor.execute("""INSERT OR IGNORE INTO user_records(claimed_email, fname, lname, title, dept)
                            VALUES (?,?,?,?,?)""", (self.email_box.text(), self.fname_box.text(), self.lname_box.text(),
                                                    self.title_box.text(), self.dept_box.text()))
        self.connection.commit()
        self.email_box.setStyleSheet("background-color: green")
