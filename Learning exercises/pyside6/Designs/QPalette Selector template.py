
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QPushButton, QVBoxLayout, QLabel, QComboBox
    )       
from PySide6.QtGui import QPalette, QColor     
from PySide6.QtCore import Qt

class Palettes():

    @staticmethod # This allows you to call the method on the class itself without needing an instance. Useful for utility methods that don't modify the state of the class or instance.
    def dark_palette():
        # Template obtained from "Create GUI Applications with Python Qt6" Book, page 192. 
        # This palette is mostly done by Jürgen Skrotzky 

        darkPalette = QPalette()

        # Setting colors for different UI elements in the palette
        darkPalette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
        darkPalette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
        darkPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(127, 127, 127))
        darkPalette.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))
        darkPalette.setColor(QPalette.ColorRole.AlternateBase, QColor(66, 66, 66))
        darkPalette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
        darkPalette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
        darkPalette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
        darkPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(127, 127, 127))
        darkPalette.setColor(QPalette.ColorRole.Dark, QColor(35, 35, 35))
        darkPalette.setColor(QPalette.ColorRole.Shadow, QColor(20, 20, 20))
        darkPalette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        darkPalette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
        darkPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(127, 127, 127))
        darkPalette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
        darkPalette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(80, 80, 80))
        darkPalette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.white)
        darkPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))

        return darkPalette

    @staticmethod
    def light_palette():
        lightPalette = QPalette()
        lightPalette.setColor(QPalette.ColorRole.Window, QColor(245, 245, 245))
        lightPalette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.black)
        lightPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(127, 127, 127))
        lightPalette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
        lightPalette.setColor(QPalette.ColorRole.AlternateBase, QColor(240, 240, 240))
        lightPalette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
        lightPalette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.black)
        lightPalette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.black)
        lightPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(127, 127, 127))
        lightPalette.setColor(QPalette.ColorRole.Dark, QColor(160, 160, 160))
        lightPalette.setColor(QPalette.ColorRole.Shadow, QColor(105, 105, 105))
        lightPalette.setColor(QPalette.ColorRole.Button, QColor(220, 220, 220))
        lightPalette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.black)
        lightPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(127, 127, 127))
        lightPalette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
        lightPalette.setColor(QPalette.ColorRole.Link, QColor(0, 0, 255))
        lightPalette.setColor(QPalette.ColorRole.Highlight, QColor(0, 120, 215))
        lightPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(190, 190, 190))
        lightPalette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.white)
        lightPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))
    
        return lightPalette

    @staticmethod
    def neon_palette():
        neonPalette = QPalette()
        neonPalette.setColor(QPalette.ColorRole.Window, QColor(20, 20, 20))
        neonPalette.setColor(QPalette.ColorRole.WindowText, QColor(57, 255, 20))  # Neon Green
        neonPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(127, 127, 127))
        neonPalette.setColor(QPalette.ColorRole.Base, QColor(0, 0, 0))
        neonPalette.setColor(QPalette.ColorRole.AlternateBase, QColor(30, 30, 30))
        neonPalette.setColor(QPalette.ColorRole.ToolTipBase, QColor(0, 0, 0))
        neonPalette.setColor(QPalette.ColorRole.ToolTipText, QColor(57, 255, 20))
        neonPalette.setColor(QPalette.ColorRole.Text, QColor(57, 255, 20))
        neonPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(127, 127, 127))
        neonPalette.setColor(QPalette.ColorRole.Dark, QColor(20, 20, 20))
        neonPalette.setColor(QPalette.ColorRole.Shadow, QColor(10, 10, 10))
        neonPalette.setColor(QPalette.ColorRole.Button, QColor(0, 0, 0))
        neonPalette.setColor(QPalette.ColorRole.ButtonText, QColor(57, 255, 20))
        neonPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(127, 127, 127))
        neonPalette.setColor(QPalette.ColorRole.BrightText, QColor(150, 0, 150))  # Neon Pink
        neonPalette.setColor(QPalette.ColorRole.Link, QColor(0, 150, 150))  # Neon Cyan
        neonPalette.setColor(QPalette.ColorRole.Highlight, QColor(55, 60, 55))  
        neonPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(80, 80, 80))
        neonPalette.setColor(QPalette.ColorRole.HighlightedText, QColor(57, 255, 20))
        neonPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))
        return neonPalette

    @staticmethod
    def neon_red_palette():
        neonRedPalette = QPalette()
        neonRedPalette.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))  # Dark gray
        neonRedPalette.setColor(QPalette.ColorRole.WindowText, QColor(255, 204, 204))  # Light neon red
        neonRedPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(127, 127, 127))
        neonRedPalette.setColor(QPalette.ColorRole.Base, QColor(20, 20, 20))  # Very dark gray
        neonRedPalette.setColor(QPalette.ColorRole.AlternateBase, QColor(50, 50, 50))  # Medium dark gray
        neonRedPalette.setColor(QPalette.ColorRole.ToolTipBase, QColor(30, 30, 30))  # Dark gray
        neonRedPalette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 204, 204))  # Light neon red
        neonRedPalette.setColor(QPalette.ColorRole.Text, QColor(255, 204, 204))  # Light neon red
        neonRedPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(127, 127, 127))
        neonRedPalette.setColor(QPalette.ColorRole.Dark, QColor(15, 15, 15))  # Very dark gray
        neonRedPalette.setColor(QPalette.ColorRole.Shadow, QColor(10, 10, 10))  # Very dark gray
        neonRedPalette.setColor(QPalette.ColorRole.Button, QColor(30, 30, 30))  # Dark gray
        neonRedPalette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 204, 204))  # Light neon red
        neonRedPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(127, 127, 127))
        neonRedPalette.setColor(QPalette.ColorRole.BrightText, QColor(255, 102, 102))  # Light neon pink
        neonRedPalette.setColor(QPalette.ColorRole.Link, QColor(255, 102, 102))  # Light neon pink
        neonRedPalette.setColor(QPalette.ColorRole.Highlight, QColor(255, 102, 102))  # Light neon pink
        neonRedPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(80, 80, 80))
        neonRedPalette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 204, 204))  # Light neon red
        neonRedPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))

        # Additional roles for a more complete palette
        neonRedPalette.setColor(QPalette.ColorRole.Light, QColor(60, 60, 60))
        neonRedPalette.setColor(QPalette.ColorRole.Midlight, QColor(45, 45, 45))
        neonRedPalette.setColor(QPalette.ColorRole.Mid, QColor(35, 35, 35))
        return neonRedPalette

class MainWindow(QMainWindow):  
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("MainWindow App")

        central_widget = QWidget(self) 
        self.setCentralWidget(central_widget) 
        layout = QVBoxLayout(central_widget) 

        title_label = QLabel("Test")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        self.combo_box = QComboBox()
        self.populate_combo_box()
        layout.addWidget(self.combo_box)

        self.button = QPushButton("Apply Palette")
        self.button.clicked.connect(self.change_palette)
        layout.addWidget(self.button)
    
    def populate_combo_box(self):
        self.palette_methods = {} # Initialize a dictionary to store palette method references
        
        self.combo_box.addItem("System Default")

        for attr_name in dir(Palettes): # Loop that iterates over all attribute names in 'Palettes' class
            # 'attr_name'variable takes on each attribute name (as a string) in turn (e.g., "dark_palette").

            attr = getattr(Palettes, attr_name) # Retrieves the attribute object (e.g., a method or property) from 'Palettes' class using its name.
                # The variable 'attr' stores them using getattr
                    # e.g., If attr_name is "dark_palette", then attr will be the dark_palette method.
                # 'getattr' function in Python is a built-in function used to retrieve the value of an attribute from an object by name. 
                    # getattr(object, name[, default])

            if callable(attr) and attr_name.endswith('_palette'): # Check if the attribute is a callable method and ends with '_palette'
                self.palette_methods[attr_name] = attr # Add the method to the palette_methods dictionary.
                self.combo_box.addItem(attr_name.replace('_palette', '').capitalize() + ' Palette') # Add the palette name to the combo box (formatted nicely)

    def change_palette(self):
        selected_palette_name = self.combo_box.currentText().replace(' Palette', '').lower() + '_palette' # Get the selected palette name from the combo box, convert to method name format
        
        if selected_palette_name == 'system default_palette':  # Check if the system default palette is selected
            app.setPalette(QApplication.style().standardPalette())  # Reset to the system default palette
        else:
            palette_method = self.palette_methods.get(selected_palette_name) # Get the corresponding method from the palette_methods dictionary
            if palette_method: # If the method exists, apply the palette
                app.setPalette(palette_method())

        print(f"Theme changed to: {selected_palette_name}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    app.setPalette(QApplication.style().standardPalette())
    window = MainWindow()
    window.show() 
    app.exec() 
