from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QLineEdit, QCheckBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, \
    QGridLayout, QApplication
# When finished, change import * to individually import elements
import sqlite3

import database_setup


class Window(QtWidgets.QWidget):
    def __init__(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        super().__init__()

        self.db_connection = connection
        self.db_cursor = cursor

        self.prefix_label = QLabel("Prefix: ")
        self.prefix_box = QLineEdit()

        self.fname_label = QLabel("First Name: ")
        self.fname_box = QLineEdit()

        self.lname_label = QLabel("Last Name: ")
        self.lname_box = QLineEdit()

        self.title_label = QLabel("Title: ")
        self.title_box = QLineEdit()

        self.org_label = QLabel("Organization: ")
        self.org_box = QLineEdit()

        self.email_label = QLabel("Email: ")
        self.email_box = QLineEdit()

        self.org_site_label = QLabel("Organization Site: ")
        self.org_site_box = QLineEdit()

        self.phone_num_label = QLabel("Phone Number: ")
        self.phone_num_box = QLineEdit()

        self.opportunities_label = QLabel("Opportunities: ")

        self.course_project_box = QCheckBox("Course Project")
        self.guest_speaker_box = QCheckBox("Guest Speaker")
        self.site_visit_box = QCheckBox("Site Visit")
        self.job_shadow_box = QCheckBox("Job Shadow")
        self.internships_box = QCheckBox("Internships")
        self.career_panel_box = QCheckBox("Career Panel")
        self.career_panel_box = QCheckBox("Career Panel")
        self.networking_event_box = QCheckBox("Networking Event")

        self.collab_time_label = QLabel("Collaboration Time:")

        self.sum2022_box = QCheckBox("Summer 2022")
        self.fall2022_box = QCheckBox("Fall 2022")
        self.spr2023_box = QCheckBox("Spring 2023")
        self.sum2023_box = QCheckBox("Summer 2023")
        self.other_box = QCheckBox("Other")

        self.permission_label_1 = QLabel("Permission to use organization name?")
        self.yes_button = QRadioButton("Yes")
        self.no_button = QRadioButton("No")
        self.further_discussion_button = QRadioButton("Further discussion is needed")

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("Form Submissions")
        self.resize(750, 500)

        quit_button = QPushButton("Close", self)
        quit_button.clicked.connect(self.close_program)
        quit_button.pos()

        nav_buttons = QHBoxLayout()
        nav_buttons.addStretch(1)  # This sets the size of the button within the box
        nav_buttons.addWidget(quit_button)

        # Set all boxes to read only, and fill with placeholder text
        self.prefix_box.setReadOnly(True)
        self.fname_box.setReadOnly(True)
        self.lname_box.setReadOnly(True)
        self.title_box.setReadOnly(True)
        self.org_box.setReadOnly(True)
        self.email_box.setReadOnly(True)
        self.org_site_box.setReadOnly(True)
        self.phone_num_box.setReadOnly(True)

        # Create a container to hold opportunities
        checkbox_box = QGridLayout()
        # Add them to the layout
        checkbox_box.addWidget(self.course_project_box, 0, 0)
        checkbox_box.addWidget(self.guest_speaker_box, 1, 0)
        checkbox_box.addWidget(self.site_visit_box, 2, 0)
        checkbox_box.addWidget(self.job_shadow_box, 3, 0)
        checkbox_box.addWidget(self.internships_box, 4, 0)
        checkbox_box.addWidget(self.career_panel_box, 5, 0)
        checkbox_box.addWidget(self.networking_event_box, 6, 0)

        # Set disabled so they can't be changed
        self.course_project_box.setDisabled(True)
        self.guest_speaker_box.setDisabled(True)
        self.site_visit_box.setDisabled(True)
        self.job_shadow_box.setDisabled(True)
        self.internships_box.setDisabled(True)
        self.career_panel_box.setDisabled(True)
        self.networking_event_box.setDisabled(True)

        # Box to hold all elements for collaboration time checkbox
        collab_time_box = QGridLayout()

        # Adding elements to layout
        collab_time_box.addWidget(self.sum2022_box, 0, 0)
        collab_time_box.addWidget(self.fall2022_box, 1, 0)
        collab_time_box.addWidget(self.spr2023_box, 2, 0)
        collab_time_box.addWidget(self.sum2023_box, 3, 0)
        collab_time_box.addWidget(self.other_box, 4, 0)

        # Setting checkboxes to be disabled so they can't be modified
        self.sum2022_box.setDisabled(True)
        self.fall2022_box.setDisabled(True)
        self.spr2023_box.setDisabled(True)
        self.sum2023_box.setDisabled(True)
        self.other_box.setDisabled(True)

        self.yes_button.setDisabled(True)
        self.no_button.setDisabled(True)
        self.further_discussion_button.setDisabled(True)

        # List that will hold the brief entry description
        entry_list = QVBoxLayout()
        # Get entries from db
        self.db_cursor.execute("""SELECT * FROM responses""")
        db_responses = self.db_cursor.fetchall()
        # Create an array to hold the entry buttons
        button_list = [None] * len(db_responses)  # this may work but have to determine number of entries here
        for i in range(10):
            # Get the entry number and organization name, put them on the button, and assign it the clicked function
            button_list[i] = QPushButton(db_responses[i][0] + ": " + db_responses[i][5])
            entry_list.addWidget(button_list[i])
            button_list[i].clicked.connect(self.show_full_information)

        # Will hold the details of one selected layout
        detailed_entry = QVBoxLayout()
        name_and_title_info = QGridLayout()

        name_and_title_info.addWidget(self.prefix_label, 0, 0)
        name_and_title_info.addWidget(self.prefix_box, 0, 1)
        name_and_title_info.addWidget(self.title_label, 0, 2)
        name_and_title_info.addWidget(self.title_box, 0, 3)

        name_and_title_info.addWidget(self.fname_label, 1, 0)
        name_and_title_info.addWidget(self.fname_box, 1, 1)
        name_and_title_info.addWidget(self.lname_label, 1, 2)
        name_and_title_info.addWidget(self.lname_box, 1, 3)

        name_and_title_info.addWidget(self.org_label, 2, 0)
        name_and_title_info.addWidget(self.org_box, 2, 1)
        name_and_title_info.addWidget(self.org_site_label, 2, 2)
        name_and_title_info.addWidget(self.org_site_box, 2, 3)

        name_and_title_info.addWidget(self.email_label, 3, 0)
        name_and_title_info.addWidget(self.email_box, 3, 1)
        name_and_title_info.addWidget(self.phone_num_label, 3, 2)
        name_and_title_info.addWidget(self.phone_num_box, 3, 3)

        name_and_title_info.addWidget(self.opportunities_label, 4, 0)
        name_and_title_info.addLayout(checkbox_box, 5, 1)

        name_and_title_info.addWidget(self.collab_time_label, 4, 2)
        name_and_title_info.addLayout(collab_time_box, 5, 3)

        name_and_title_info.addWidget(self.permission_label_1, 7, 0)
        name_and_title_info.addWidget(self.yes_button, 8, 1)
        name_and_title_info.addWidget(self.no_button, 8, 2)
        name_and_title_info.addWidget(self.further_discussion_button, 8, 3)

        # Container to hold the two halves of the menu interface
        main_list_container = QHBoxLayout()
        main_list_container.addLayout(entry_list)
        # adjust spacing once left side is finished to make it look good
        main_list_container.addSpacing(100)
        main_list_container.addLayout(detailed_entry)
        main_list_container.addLayout(name_and_title_info)

        # v_box will be the main container for everything in the window
        v_box = QVBoxLayout()
        # putting addStretch before or after addLayout determines placement
        v_box.addLayout(main_list_container)
        v_box.addStretch(1)
        v_box.addLayout(nav_buttons)

        self.setLayout(v_box)

    def show_full_information(self):
        # Call reset_checkboxes to clear time, opportunity and permission boxes
        self.reset_checkboxes()

        # Get the text on the button that was clicked
        button_text = self.sender().text()

        # Prepare a query to get the rest of the entry
        get_query = """SELECT * FROM responses WHERE entryNum = ?"""

        pkey = button_text.split(":")

        # Pass the number on the button to the query, as it is the primary key
        self.db_cursor.execute(get_query, (pkey[0],))

        # (pkey[0],) in above line was taken from
        # https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
        # This allowed two-digit numbers to be passed correctly

        # Get the response from db
        selected_response = self.db_cursor.fetchall()

        # Set the text boxes
        self.prefix_box.setText(selected_response[0][1])
        self.fname_box.setText(selected_response[0][2])
        self.lname_box.setText(selected_response[0][3])
        self.title_box.setText(selected_response[0][4])
        self.org_box.setText(selected_response[0][5])
        self.email_box.setText(selected_response[0][6])
        self.org_site_box.setText(selected_response[0][7])
        self.phone_num_box.setText(selected_response[0][8])

        # Set the checkboxes
        match selected_response[0][9]:
            case "Course Project":
                self.course_project_box.setChecked(True)
            case "Guest Speaker":
                self.guest_speaker_box.setChecked(True)
            case "Site Visit":
                self.site_visit_box.setChecked(True)
            case "Job Shadow":
                self.job_shadow_box.setChecked(True)
            case "Internships":
                self.internships_box.setChecked(True)
            case "Career Panel":
                self.career_panel_box.setChecked(True)
            case "Networking Event":
                self.networking_event_box.setChecked(True)
            case _:
                pass

        match selected_response[0][10]:
            case "Summer 2022":
                self.sum2022_box.setChecked(True)
            case "Fall 2022":
                self.fall2022_box.setChecked(True)
            case "Spring 2023":
                self.spr2023_box.setChecked(True)
            case "Summer 2023":
                self.sum2023_box.setChecked(True)
            case "Other":
                self.other_box.setChecked(True)
            case _:
                pass

        match selected_response[0][11]:
            case "Yes":
                self.yes_button.setChecked(True)
            case "No":
                self.no_button.setChecked(True)
            case "Further discussion is needed":
                self.further_discussion_button.setChecked(True)
            case _:
                pass

    def reset_checkboxes(self):
        # Resets all checkboxes when a new entry is selected
        self.course_project_box.setChecked(False)
        self.guest_speaker_box.setChecked(False)
        self.site_visit_box.setChecked(False)
        self.job_shadow_box.setChecked(False)
        self.internships_box.setChecked(False)
        self.career_panel_box.setChecked(False)
        self.networking_event_box.setChecked(False)

        self.sum2022_box.setChecked(False)
        self.fall2022_box.setChecked(False)
        self.spr2023_box.setChecked(False)
        self.sum2023_box.setChecked(False)
        self.other_box.setChecked(False)

        self.yes_button.setChecked(False)
        self.no_button.setChecked(False)
        self.further_discussion_button.setChecked(False)

    def close_program(self):
        database_setup.close_db(self.db_connection)
        QApplication.instance().quit()
