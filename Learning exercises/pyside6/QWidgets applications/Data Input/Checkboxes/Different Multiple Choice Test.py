from PySide6.QtWidgets import QWidget, QApplication, QCheckBox, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton,QButtonGroup
import sys

    
class Widget(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("QCheckBox and QRadioButton")

    # Non-Exclusive Checkboxes group
        # it requires creating a groupbox, a container of boxes.
        # checkboxes can be independent from one another such as the following:
        Checkboxes = QGroupBox("Checkboxes")

        Checkbox_1 = QCheckBox("Option 1")
        Checkbox_1.toggled.connect(self.Checkbox_1_Toggled)

        Checkbox_2 = QCheckBox("Option 2")
        Checkbox_2.toggled.connect(self.Checkbox_2_Toggled)

        Checkbox_3 = QCheckBox("Option 3")
        Checkbox_3.toggled.connect(self.Checkbox_3_Toggled)

        Checkboxes_layout = QVBoxLayout()
        Checkboxes_layout.addWidget(Checkbox_1)
        Checkboxes_layout.addWidget(Checkbox_2)
        Checkboxes_layout.addWidget(Checkbox_3)
        Checkboxes.setLayout(Checkboxes_layout)

    # Exclusive checkboxes
        Ex_Checkboxes = QGroupBox("Choose one option") # we set up the group box
        # then we set up the options
        Ex_Checkbox1 = QCheckBox("Ex_Checkbox1")
        Ex_Checkbox2 = QCheckBox("Ex_Checkbox2")
        Ex_Checkbox3 = QCheckBox("Ex_Checkbox3")
        Ex_Checkbox1.setChecked(True) # we set up the first option checked by default

        #Make the checkboxes exclusive
        exclusive_button_group = QButtonGroup(self) # The self parent is needed here.
        exclusive_button_group.addButton(Ex_Checkbox1)
        exclusive_button_group.addButton(Ex_Checkbox2)
        exclusive_button_group.addButton(Ex_Checkbox3)
        exclusive_button_group.setExclusive(True)

        Ex_checkboxes_Layout = QVBoxLayout()
        Ex_checkboxes_Layout.addWidget(Ex_Checkbox1)
        Ex_checkboxes_Layout.addWidget(Ex_Checkbox2)
        Ex_checkboxes_Layout.addWidget(Ex_Checkbox3)
        Ex_Checkboxes.setLayout(Ex_checkboxes_Layout)

    # Radio buttons : answers
        answers = QGroupBox("Choose Answer")
        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")
        answer_a.setChecked(True)

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)
        answers.setLayout(answers_layout)


        h_layout = QHBoxLayout()
        h_layout.addWidget(Checkboxes)
        h_layout.addWidget(Ex_Checkboxes)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answers)

        self.setLayout(v_layout)

    # Actions when clicked
    def Checkbox_1_Toggled(self,checked): 
            if(checked):
                print("Checkbox_1 checked")
            else:
                print("Checkbox_1 unchecked")

    def Checkbox_2_Toggled(self,checked): 
            if(checked):
                print("Checkbox_2 checked")
            else:
                print("Checkbox_2 unchecked")

    def Checkbox_3_Toggled(self,checked): 
            if(checked):
                print("Checkbox_3 checked")
            else:
                print("Checkbox_3 unchecked")

app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()