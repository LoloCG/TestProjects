from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMainWindow
from Widgets.UI_MWindow import Ui_MainAppWindow
from Widgets.UI_VideoQuery import Ui_VideoForm
from Widgets.UI_AboutWindow import Ui_AboutDialog
from MainTableWidget import Ui_MainTableWidget

class MainWindow(QMainWindow, Ui_MainAppWindow): # QMainWindow is required instead of QWidget, as setCentralWidget is part of the first one.
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Media Database")

        self.actionMovie.triggered.connect(self.ShowVideoQuery)
        self.actionAbout.triggered.connect(self.ShowAboutDialog)

        data = [
            ["Test1a", "test1b", "test1c"],
            ["Test2a", "test2b", "test2c"],
            ["Test3a", "test3b", "test3c"],
        ]
        
        self.main_table_widget = Ui_MainTableWidget()
        #self.verticalLayout.replaceWidget(self.main_table_placeholder, self.main_table_widget) # replaces the placeholder with the table

    def ShowVideoQuery(self):
        print("showing video query")
        self.video_query_window = VideoQuery()
        self.video_query_window.show()
        self.video_query_window.raise_()  # Bring the window to the front

    def ShowAboutDialog(self):
        print("Showing About Dialog")
        self.Show_About_Dialog = AboutDialog()
        self.Show_About_Dialog.show()
        self.Show_About_Dialog.raise_()


class VideoQuery(QWidget, Ui_VideoForm):
       def __init__(self):
        super().__init__()
        self.setupUi(self) 
        #self.setWindowTitle("Video Query"
        self.CancelButton.clicked.connect(self.close)


class AboutDialog(QWidget, Ui_AboutDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.AboutAcceptButton.clicked.connect(self.close)
    