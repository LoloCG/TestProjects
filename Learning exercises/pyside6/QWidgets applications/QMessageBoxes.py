from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
import sys

class Widget(QWidget):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("MessageBox Test")
        
            button_hard = QPushButton("Hard")
            button_hard.clicked.connect(self.button_clicked_hard)

            button_critical = QPushButton("Critical")
            button_critical.clicked.connect(self.button_clicked_critical)

            button_question = QPushButton("Question")
            button_question.clicked.connect(self.button_clicked_question)

            button_information = QPushButton("Information")
            button_information.clicked.connect(self.button_clicked_information)

            button_warning = QPushButton("Warning")
            button_warning.clicked.connect(self.button_clicked_warning)

            button_about = QPushButton("About")
            button_about.clicked.connect(self.button_clicked_about)

            layout = QVBoxLayout()
            layout.addWidget(button_hard)
            layout.addWidget(button_critical)
            layout.addWidget(button_question)
            layout.addWidget(button_information)
            layout.addWidget(button_warning)
            layout.addWidget(button_about)
            self.setLayout(layout)

    # The hard way method to create message boxes.
        def button_clicked_hard(self):
            message = QMessageBox() # creates the message box object
            message.setMinimumSize(700, 200)
            message.setWindowTitle("Message Title")
            message.setText("Something happened")
            message.setInformativeText("Do you want to do something about it?")
            message.setIcon(QMessageBox.Critical) # this icon can be changed to other types
            message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            message.setDefaultButton(QMessageBox.Ok)
            ret = message.exec() # this uses the exec method to show the message box. 
            if ret == QMessageBox.Ok:
                print("User chose OK")
            else:
                print("User chose Cancel")

    # Static Messagebox Methods
        # Can be: critical - question - information - warning - about
        # the main difference is the sound it makes and the icon shown along with it.
        def button_clicked_critical(self):
            ret = QMessageBox.critical(self, "Message Title", "Critical Message!", QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Ok:
                print("User chose OK")
            else:
                print("User chose Cancel")


        def button_clicked_question(self):
            ret = QMessageBox.question(self, "Message Title", "Some information",
                                        QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Ok:
                print("User chose OK")
            else:
                print("User chose Cancel")

        def button_clicked_information(self):
            ret = QMessageBox.information(self, "Message Title", "Some information",
                                        QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Ok:
                print("User chose OK")
            else:
                print("User chose Cancel")

        def button_clicked_warning(self):
            ret = QMessageBox.warning(self, "warning Title", "Some information",
                                        QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Ok:
                print("User chose OK")
            else:
                print("User chose Cancel")
            
        # this is the only one that does not require setting up button options
        def button_clicked_about(self):
            ret = QMessageBox.about(self, "Message Title", "Some about information")
            if ret == QMessageBox.Ok:
                print("User chose OK")
            else:
                print("User chose Cancel")


    # Static Messagebox Methods
    # Can be
    # critical - question - information - warning - about

'''
button_clicked_question
# Information
    def button_clicked_information(self):
        ret = QMessageBox.information(self, "Message Title", "Some information",
                                    QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Cancel")

    # About
    def button_clicked_about(self):
        ret = QMessageBox.about(self, "Message Title", "Some about message")
        if ret == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Cancel")
'''

app = QApplication(sys.argv)
widget = Widget()
widget.show()
app.exec()
