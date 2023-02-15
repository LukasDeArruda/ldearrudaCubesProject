from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
# When finished, change import * to individually import elements
import sys


class MockupWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("Form Submissions")
        self.resize(750, 500)

        quit_button = QPushButton("Close", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.pos()

        nav_buttons = QHBoxLayout()
        nav_buttons.addStretch(1)  # This sets the size of the button within the box
        nav_buttons.addWidget(quit_button)

        prefix_label = QLabel("Prefix: ")
        prefix_box = QLineEdit()
        prefix_box.setReadOnly(True)
        prefix_box.setText("Prefix")

        fname_label = QLabel("First Name: ")
        fname_box = QLineEdit()
        fname_box.setReadOnly(True)
        fname_box.setText("First Name")

        lname_label = QLabel("Last Name: ")
        lname_box = QLineEdit()
        lname_box.setReadOnly(True)
        lname_box.setText("Last Name")

        title_label = QLabel("Title: ")
        title_box = QLineEdit()
        title_box.setReadOnly(True)
        title_box.setText("Title")

        org_label = QLabel("Organization: ")
        org_box = QLineEdit()
        org_box.setReadOnly(True)
        org_box.setText("Organization")

        email_label = QLabel("Email: ")
        email_box = QLineEdit()
        email_box.setReadOnly(True)
        email_box.setText("Email Address")

        org_site_label = QLabel("Organization Site: ")
        org_site_box = QLineEdit()
        org_site_box.setReadOnly(True)
        org_site_box.setText("Organization Site")

        phone_num_label = QLabel("Phone Number: ")
        phone_num_box = QLineEdit()
        phone_num_box.setReadOnly(True)
        phone_num_box.setText("Phone Number")

        opportunites_label = QLabel("Opportunities: ")

        checkbox_box = QGridLayout()
        course_project_box = QCheckBox("Course Project")
        course_project_box.setDisabled(True)
        guest_speaker_box = QCheckBox("Guest Speaker")
        guest_speaker_box.setDisabled(True)
        site_visit_box = QCheckBox("Site Visit")
        site_visit_box.setDisabled(True)
        job_shadow_box = QCheckBox("Job Shadow")
        job_shadow_box.setDisabled(True)
        internships_box = QCheckBox("Internships")
        internships_box.setDisabled(True)
        career_panel_box = QCheckBox("Career Panel")
        career_panel_box.setDisabled(True)
        networking_event_box = QCheckBox("Networking Event")
        networking_event_box.setDisabled(True)

        checkbox_box.addWidget(course_project_box, 0, 0)
        checkbox_box.addWidget(guest_speaker_box, 1, 0)
        checkbox_box.addWidget(site_visit_box, 2, 0)
        checkbox_box.addWidget(job_shadow_box, 3, 0)
        checkbox_box.addWidget(internships_box, 4, 0)
        checkbox_box.addWidget(career_panel_box, 5, 0)
        checkbox_box.addWidget(networking_event_box, 6, 0)

        collab_time_label = QLabel("Collaboration Time:")

        collab_time_box = QGridLayout()
        sum2022_box = QCheckBox("Summer 2022")
        sum2022_box.setDisabled(True)
        fall2022_box = QCheckBox("Fall 2022")
        fall2022_box.setDisabled(True)
        spr2023_box = QCheckBox("Spring 2023")
        spr2023_box.setDisabled(True)
        sum2023_box = QCheckBox("Summer 2023")
        sum2023_box.setDisabled(True)
        other_box = QCheckBox("Other")
        other_box.setDisabled(True)

        collab_time_box.addWidget(sum2022_box, 0, 0)
        collab_time_box.addWidget(fall2022_box, 1, 0)
        collab_time_box.addWidget(spr2023_box, 2, 0)
        collab_time_box.addWidget(sum2023_box, 3, 0)
        collab_time_box.addWidget(other_box, 4, 0)

        permission_label = QLabel("Permission to use organization name?")
        yes_button = QRadioButton("Yes")
        yes_button.setDisabled(True)
        no_button = QRadioButton("No")
        no_button.setDisabled(True)

        # List that will hold the brief entry description
        entry_list = QVBoxLayout()
        button_list = [None] * 10  # this may work but have to determine number of entries here
        for i in range(10):
            button_list[i] = QPushButton("Test " + str(i))
            entry_list.addWidget(button_list[i])
            button_list[i].clicked.connect(self.button_clicked)

        # Will hold the details of one selected layout
        detailed_entry = QVBoxLayout()
        name_and_title_info = QGridLayout()

        name_and_title_info.addWidget(prefix_label, 0, 0)
        name_and_title_info.addWidget(prefix_box, 0, 1)
        name_and_title_info.addWidget(title_label, 0, 2)
        name_and_title_info.addWidget(title_box, 0, 3)

        name_and_title_info.addWidget(fname_label, 1, 0)
        name_and_title_info.addWidget(fname_box, 1, 1)
        name_and_title_info.addWidget(lname_label, 1, 2)
        name_and_title_info.addWidget(lname_box, 1, 3)

        name_and_title_info.addWidget(org_label, 2, 0)
        name_and_title_info.addWidget(org_box, 2, 1)
        name_and_title_info.addWidget(org_site_label, 2, 2)
        name_and_title_info.addWidget(org_site_box, 2, 3)

        name_and_title_info.addWidget(email_label, 3, 0)
        name_and_title_info.addWidget(email_box, 3, 1)
        name_and_title_info.addWidget(phone_num_label, 3, 2)
        name_and_title_info.addWidget(phone_num_box, 3, 3)

        name_and_title_info.addWidget(opportunites_label, 4, 0)
        name_and_title_info.addLayout(checkbox_box, 5, 1)

        name_and_title_info.addWidget(collab_time_label, 4, 2)
        name_and_title_info.addLayout(collab_time_box, 5, 3)

        name_and_title_info.addWidget(permission_label, 7, 0)
        name_and_title_info.addWidget(yes_button, 8, 1)
        name_and_title_info.addWidget(no_button, 8, 2)

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

    def button_clicked(self):
        # the plan is to use the information we put into the button label in order to create
        # an sql query to get the rest of the data

        # use QCheckBox.setChecked(True) to toggle boxes
        print(self.sender().text())


def main():
    app = QtWidgets.QApplication()
    main_window = MockupWindow()
    main_window.show()
    sys.exit(app.exec())


main()
