import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QApplication, # QApplication is required for the main python file.
    QMainWindow, # QMainWindow only for the main window that will contain future widgets. Others can be QWidget
    QPushButton, QLabel, QVBoxLayout, QWidget
)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow): # Creates a class that inherits from QMainWindow. It can be separated further into another file.
    def __init__(self): # The constructor
        super().__init__()

        self.setWindowTitle("MainWindow App")

        central_widget = QWidget(self) # Creates a central widget that will contain other widgets
        self.setCentralWidget(central_widget) # Set it as the central widget
        layout = QVBoxLayout(central_widget) # Creates a vertical layout for the central widget

        # We create the the label, align it to the center, and add them to the layout
        title_label = QLabel("Test")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Similar as the title but with the button.
        button = QPushButton("button")
        layout.addWidget(button)

# This block is used to ensure that certain parts of code only run when the script is executed directly, 
# not when it is imported as a module in another script.
# Key benefits:
# - Encapsulation: Wrapping the application logic in a class (MainWindow) makes the code more modular, reusable, and easier to maintain.
# - 'if __name__ == "__main__":': Ensures that the script can be safely imported as a module without running the main application code, facilitating better modularization and testing.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show() # by default, widgets are hidden unless shown
    app.exec() # Starts the event loop
