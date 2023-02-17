from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
# When finished, change import * to individually import elements
import sys


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

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

        self.opportunites_label = QLabel("Opportunities: ")

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

        self.permission_label = QLabel("Permission to use organization name?")
        self.yes_button = QRadioButton("Yes")
        self.no_button = QRadioButton("No")

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

        # Set all boxes to read only, and fill with placeholder text
        self.prefix_box.setReadOnly(True)
        self.prefix_box.setText("Prefix")

        self.fname_box.setReadOnly(True)
        self.fname_box.setText("First Name")

        self.lname_box.setReadOnly(True)
        self.lname_box.setText("Last Name")

        self.title_box.setReadOnly(True)
        self.title_box.setText("Title")

        self.org_box.setReadOnly(True)
        self.org_box.setText("Organization")

        self.email_box.setReadOnly(True)
        self.email_box.setText("Email Address")

        self.org_site_box.setReadOnly(True)
        self.org_site_box.setText("Organization Site")

        self.phone_num_box.setReadOnly(True)
        self.phone_num_box.setText("Phone Number")

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

        # List that will hold the brief entry description
        entry_list = QVBoxLayout()
        button_list = [None] * 10  # this may work but have to determine number of entries here
        for i in range(10):
            button_list[i] = QPushButton("Test " + str(i))
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

        name_and_title_info.addWidget(self.opportunites_label, 4, 0)
        name_and_title_info.addLayout(checkbox_box, 5, 1)

        name_and_title_info.addWidget(self.collab_time_label, 4, 2)
        name_and_title_info.addLayout(collab_time_box, 5, 3)

        name_and_title_info.addWidget(self.permission_label, 7, 0)
        name_and_title_info.addWidget(self.yes_button, 8, 1)
        name_and_title_info.addWidget(self.no_button, 8, 2)

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
        # the plan is to use the information we put into the button label in order to create
        # an sql query to get the rest of the data

        # use QCheckBox.setChecked(True) to toggle boxes
        self.prefix_box.setText("Updated")
        self.fname_box.setText("Updated")
        self.lname_box.setText("Updated")
        self.title_box.setText("Updated")
        self.org_box.setText("Updated")
        self.email_box.setText("Updated")
        self.org_site_box.setText("Updated")
        self.phone_num_box.setText("Updated")
        self.course_project_box.setChecked(True)
        self.sum2022_box.setChecked(True)
        self.yes_button.setChecked(True)
        print(self.sender().text())
