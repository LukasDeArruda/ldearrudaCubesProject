from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel


class PopupWindow(QtWidgets.QDialog):
    def __init__(self, message: QLabel):
        super().__init__()

        self.window_message = message

        self.ok_button = QPushButton("Ok")
        self.ok_button.clicked.connect(self.close)

        self.build_window()

    def build_window(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.window_message)
        main_layout.addWidget(self.ok_button)

        self.setLayout(main_layout)
        self.show()


