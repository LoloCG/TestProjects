from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class SecondaryWidget1(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout(self)
        self.back_button = QPushButton("Back to Main Menu")
        layout.addWidget(self.back_button)
        self.back_button.clicked.connect(self.go_back)

    def go_back(self):
        self.main_window.show_main_menu()
