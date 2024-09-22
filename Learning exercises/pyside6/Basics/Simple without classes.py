import sys # module responsible for processing command line arguments.
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout)
from PySide6.QtCore import Qt

app = QApplication(sys.argv) # Command line argument. Is the wrapper responsible for running the application and waiting for things to happen while we interact with the application
window = QMainWindow() # This can be QMainWindow or QWidget

central_widget = QWidget() # Create a central widget that will contain other widgets
window.setCentralWidget(central_widget) # Set the central widget
layout = QVBoxLayout(central_widget) # Create a vertical layout for the central widget

title_label = QLabel("Test")
title_label.setAlignment(Qt.AlignCenter)
layout.addWidget(title_label)

button = QPushButton("button")
layout.addWidget(button)

window.show() # by default, widgets are hidden unless shown
app.exec() # Starts the event loop