#from PySide6.QtWidgets import 
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
        neonPalette.setColor(QPalette.ColorRole.Base, QColor(5, 5, 5))
        neonPalette.setColor(QPalette.ColorRole.AlternateBase, QColor(15, 15, 15))
        neonPalette.setColor(QPalette.ColorRole.ToolTipBase, QColor(0, 0, 0))
        neonPalette.setColor(QPalette.ColorRole.ToolTipText, QColor(57, 255, 20))
        neonPalette.setColor(QPalette.ColorRole.Text, QColor(57, 255, 20))
        neonPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(127, 127, 127))
        neonPalette.setColor(QPalette.ColorRole.Dark, QColor(20, 20, 20))
        neonPalette.setColor(QPalette.ColorRole.Shadow, QColor(10, 10, 10))
        neonPalette.setColor(QPalette.ColorRole.Button, QColor(0, 0, 0))
        neonPalette.setColor(QPalette.ColorRole.ButtonText, QColor(57, 255, 20))
        neonPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(127, 127, 127))
        neonPalette.setColor(QPalette.ColorRole.BrightText, QColor(150, 0, 150))  
        neonPalette.setColor(QPalette.ColorRole.Link, QColor(0, 150, 150)) 
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
