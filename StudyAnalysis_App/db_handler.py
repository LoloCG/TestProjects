'''
About this file:
    It will contain as a module, all the important classes and functions related to the database generation, querying, etc.

MVP:
    - Function to detect if database exists
    - Function to check if there new data is found from the source (e.g.: a CSV file) compared to the database
    - Function to update database with the new data from the source.

'''
import sqlite3

class DatabaseHandler:
    def __init__(self):
        self.connector = None
        self.database_name = None
        self.cursor = None

    def settup_db(db_name=None):
        if db_name is None: # If database does not exist, create one.
            db_name = 'Database.db'
        # elif db_name # if database does not contain '.db', add it at the end

        self.database_name = db_name
        self.connector = sqlite3.connect(self.database_name)
        self.cursor = self.connector.cursor()

    def setup_db_table(self, tableItems):
        # maybe create a dictionary with key being the title of each column, and the contents being the data type
        if self.database_name is None:
            self.settup_db()

        self.connector = sqlite3.connect(self.database_name)
        self.cursor = self.connector.cursor()

        columns = ", ".join([f"{col} {dtype}" for col, dtype in tableItems.items()])

        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {columns}
        )
        '''
        self.cursor.execute(create_table_query)

        self.connector.commit()  # Save the changes to the database
    

    def check_db_existance():
        if self.database_name is None:
            print("No database has been set up yet.")
            return False
        return os.path.exists(self.database_name)
    
    def check_db_isupdated(self, newData):
        if self.database_name is None:
            self.settup_db()

        self.connector = sqlite3.connect(self.database_name)
        self.cursor = self.connector.cursor()

        # Assuming we're checking for updated schema or new columns
        existing_columns = [description[0] for description in self.cursor.execute("PRAGMA table_info(tasks)").fetchall()]
        new_columns = list(newData.keys())
        
        return set(existing_columns) == set(new_columns)

    def update_db(self, newData):
        if self.database_name is None:
            self.settup_db()

        if not self.check_db_isupdated(newData):
            # Add any new columns
            for col, dtype in newData.items():
                self.cursor.execute(f"ALTER TABLE tasks ADD COLUMN {col} {dtype}")

        # To update rows, you'll need to have a method of identifying the rows to update,
        # such as an ID or another unique identifier. Example given is for adding/updating a row.
        keys = ", ".join(newData.keys())
        question_marks = ", ".join(["?" for _ in newData])
        values = tuple(newData.values())
        insert_query = f"INSERT INTO tasks ({keys}) VALUES ({question_marks})"
        self.cursor.execute(insert_query, values)
        self.connector.commit()

    def close_connection(self):
        if self.connector:
            self.connector.close()
