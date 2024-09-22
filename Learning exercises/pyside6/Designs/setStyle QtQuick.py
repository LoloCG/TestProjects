import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, 
    QVBoxLayout, QLabel, QWidget,
    QPushButton, QComboBox, QStyleFactory
    )

class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__() 

        self.setWindowTitle("MainWindow App")

    # Create the central widget, set it as central and set the layout from it
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)  
        layout = QVBoxLayout(central_widget) 

    # We create the the label
        title_label = QLabel("Theme test")
        title_label.setAlignment(Qt.AlignCenter) 
        layout.addWidget(title_label)

    # We obtain the themes that are available
        av_themes = QStyleFactory.keys()
        print("Available themes:")
        print(av_themes)
    
    # Create the combo box and add each theme into it, then place it into the layout. 
        self.combo_box = QComboBox() # Make this an instance variable
        for theme in av_themes:
            self.combo_box.addItem(theme)
        layout.addWidget(self.combo_box)

    # Add and connect the buttons
        button = QPushButton("Apply theme")
        layout.addWidget(button)
        button.clicked.connect(self.Change_Theme)

    def Change_Theme(self):
        theme = self.combo_box.currentText()
        print("theme changed to:")
        print(theme)
        
        app.setStyle(theme)
        #QApplication.setStyle(QStyleFactory.create(theme)) This or the one before it accomplishes the same purposes

#sys.argv += ['-platform', 'windows:darkmode=2'] # Sets dark theme. Is required to be before the line "app = QApplication(sys.argv)".
app = QApplication(sys.argv)
app.setStyle('fusion') # Sets the default style as fusion

window = MainWindow()
window.show()
app.exec()