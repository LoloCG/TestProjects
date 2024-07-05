from PySide6.QtWidgets import (
    QComboBox,
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QMessageBox
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import os
import sqlite3

class QueryWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window  
        layout = QVBoxLayout(self)

        self.title_label = QLabel("Data Entry Form")
        self.title_label.setAlignment(Qt.AlignCenter)
        font = self.title_label.font()
        font.setPointSize(14)
        font.setBold(True)
        self.title_label.setFont(font)
        layout.addWidget(self.title_label)

        self.media_name_label = QLabel("Name:")
        self.media_name_input = QLineEdit()

        self.media_type_label = QLabel("Type of media:")
        self.media_type_input = QComboBox()
        self.media_type_input.addItems(["Film", "Short", "Series", "Documentary", "Other"])

        self.recommendedby_label = QLabel("Recommended by:")
        self.recommendedby_input = QLineEdit()

        self.tags_label = QLabel("Tags:")
        self.tags_input = QLineEdit()

        layout.addWidget(self.media_name_label)
        layout.addWidget(self.media_name_input)
        layout.addWidget(self.media_type_label)
        layout.addWidget(self.media_type_input)
        layout.addWidget(self.recommendedby_label)
        layout.addWidget(self.recommendedby_input)
        layout.addWidget(self.tags_label)
        layout.addWidget(self.tags_input)

        self.submit_button = QPushButton("Submit to DataBase")
        layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.Add2DB)

        self.back_button = QPushButton("Back to Main Menu")
        layout.addWidget(self.back_button)
        self.back_button.clicked.connect(self.go_back)
        
        self.setup_database()

    def setup_database(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir, 'Media_DataBase.db')

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            SELECT name FROM sqlite_master WHERE type='table' AND name='Media_DataBase';
        ''')
        table_exists = self.cursor.fetchone()

        if not table_exists:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Media_DataBase (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    media_name TEXT NOT NULL,
                    media_type TEXT NOT NULL,
                    recommended_by TEXT NOT NULL,
                    media_tags TEXT NOT NULL
                )
            ''')
            self.conn.commit()

    def Add2DB(self):
        media_name = self.media_name_input.text()
        media_type = self.media_type_input.currentText()
        recommended_by = self.recommendedby_input.text()
        media_tags = self.tags_input.text()

        if not media_name or not media_type:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Name and type are required.")
            msg.setWindowTitle("Input Error")
            msg.exec()
            return

        self.cursor.execute('''
            SELECT * FROM Media_DataBase WHERE media_name = ? AND media_type = ?
        ''', (media_name, media_type))
        existing_item = self.cursor.fetchone()

        if existing_item:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("This item already exists in the database.")
            msg.setWindowTitle("Duplicate Entry")
            msg.exec()
            return

        self.cursor.execute('''
            INSERT INTO Media_DataBase (media_name, media_type, recommended_by, media_tags)
            VALUES (?, ?, ?, ?)
        ''', (media_name, media_type, recommended_by, media_tags))
        self.conn.commit()

        print("New item added:")
        print(f"Name: {media_name}")
        print(f"Type of Media: {media_type}")
        print(f"Recommended by: {recommended_by}")
        print(f"Tags: {media_tags}")

    def go_back(self):
        self.main_window.show_main_menu()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QueryWindow(None)
    window.show()
    sys.exit(app.exec())