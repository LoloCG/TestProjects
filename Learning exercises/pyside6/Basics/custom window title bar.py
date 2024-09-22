from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QVBoxLayout


class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.close_button = QPushButton("X")
        self.minimize_button = QPushButton("-")
        self.maximize_button = QPushButton("+")

        self.close_button.setFixedSize(25, 25)
        self.minimize_button.setFixedSize(25, 25)
        self.maximize_button.setFixedSize(25, 25)

        layout = QHBoxLayout()
        layout.addWidget(self.minimize_button)
        layout.addWidget(self.maximize_button)
        layout.addWidget(self.close_button)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

        self.close_button.clicked.connect(self.close_window)
        self.minimize_button.clicked.connect(self.minimize_window)
        self.maximize_button.clicked.connect(self.maximize_window)

    def close_window(self):
        self.window().close()

    def minimize_window(self):
        self.window().showMinimized()

    def maximize_window(self):
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.title_bar = CustomTitleBar(self)
        self.main_widget = QWidget()
        
        layout = QVBoxLayout()
        layout.addWidget(self.title_bar)
        layout.addWidget(self.main_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication([])

    main_window = MainWindow()
    main_window.show()

    app.exec()
