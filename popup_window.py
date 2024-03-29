from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel


class PopupWindow(QtWidgets.QDialog):
    def __init__(self, message: QLabel, window_title: str):
        super().__init__()

        self.window_message = message
        self.window_title = window_title

        self.ok_button = QPushButton("Ok")
        self.ok_button.clicked.connect(self.close)

        self.build_window()

    def build_window(self):
        self.setWindowTitle(self.window_title)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.window_message)
        main_layout.addWidget(self.ok_button)

        self.setLayout(main_layout)
        self.show()


