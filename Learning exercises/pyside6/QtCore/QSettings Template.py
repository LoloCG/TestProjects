import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
# Creates a window which its size gets saved in a settings file. 
# When closing and running again, the size was the last it was sized.
from PySide6.QtCore import QSettings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings = QSettings("MyApp", "AppSettings")

        self.initUI()
        self.load_settings()

    def initUI(self):
        self.setWindowTitle("QSettings Example")

        # Create a button to change the window size
        self.button = QPushButton("Resize Window", self)
        self.button.clicked.connect(self.resize_window)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def resize_window(self):
        # Resize the window to a fixed size
        self.resize(125, 100)

    def load_settings(self):
        # Load window size
        size = self.settings.value("windowSize", self.size())
        self.resize(size)

    def closeEvent(self, event):
        # Save window size
        self.settings.setValue("windowSize", self.size())
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
