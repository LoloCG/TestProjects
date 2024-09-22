import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, 
    QVBoxLayout, QLabel, QWidget,
    QGroupBox, QCheckBox, QButtonGroup
    )

class MainWindow(QMainWindow):  # We create a class, inheriting from QMainWindow
    def __init__(self): # The constructor
        super().__init__() 

    # Create the central widget, set it as central and set the layout from it
        central_widget = QWidget(self)  # Create a central widget that will contain other widgets
        self.setCentralWidget(central_widget)  # Set the central widget
        layout = QVBoxLayout(central_widget) # Create a vertical layout for the central widget

    # We create the the label and test buttons
        title_label = QLabel("Theme test")
        title_label.setAlignment(Qt.AlignCenter) # Adjust the label to the center
        layout.addWidget(title_label)
        
    # Create the checkboxes, their layout and connections
        # First we set the GroupBox, that will contain the CheckBoxes, along the checkboxes.
        Checkboxes_GroupBox = QGroupBox("Choose Option")
        Checkbox1 = QCheckBox("Option 1")
        Checkbox2 = QCheckBox("Option 2")
        Checkbox3 = QCheckBox("Option 3")
        Checkbox4 = QCheckBox("Option 4")
        Checkbox5 = QCheckBox("Option 5")
        Checkbox1.setChecked(True) # we set up the first option checked by default
        
        # Connect them to their function
        Checkbox1.toggled.connect(self.Option1_select)
        Checkbox2.toggled.connect(self.Option2_select)
        Checkbox3.toggled.connect(self.Option3_select)
            # we can continue...

        # We select the group of buttons that is exclusive, adding them to a QButtonGroup
        ex_button_group = QButtonGroup(self)
        ex_button_group.addButton(Checkbox1)
        ex_button_group.addButton(Checkbox2)
        ex_button_group.addButton(Checkbox3)
        ex_button_group.addButton(Checkbox4)
        ex_button_group.addButton(Checkbox5)
        
        # We add them to the layout
        Checkboxes_Layout = QVBoxLayout() # Create a vertical box layout for boxes and the container
        Checkboxes_Layout.addWidget(Checkbox1)
        Checkboxes_Layout.addWidget(Checkbox2)
        Checkboxes_Layout.addWidget(Checkbox3)
        Checkboxes_Layout.addWidget(Checkbox4)
        Checkboxes_Layout.addWidget(Checkbox5)
        Checkboxes_GroupBox.setLayout(Checkboxes_Layout)

        layout.addWidget(Checkboxes_GroupBox) # add that second layout to the first

    def Option1_select(self,checked):
        if(checked):
            print("Option 1")

    def Option2_select(self,checked):
        if(checked):
            print("Option 2")            

    def Option3_select(self,checked):
        if(checked):
            print("Option 2")            

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()