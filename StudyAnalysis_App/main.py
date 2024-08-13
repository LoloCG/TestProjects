import sys, os
import db_handler, hours_per_subject
from MODULE_pandas_excel_functions import ExcelDataExtract


def main_menu():
    print("Reading database...")

    chosen_file = '3º FarmNutr TDL_Log.csv'
    target_file_folder_dir = os.path.dirname(os.path.abspath(__file__)) # the file direction is the same as the script

    excelCSV_raw = ExcelDataExtract(file_folder_dir=target_file_folder_dir)
    excelCSV_raw.load_csv_to_dataframe(chosen_file)

    ''' 
    db_table = {}
    mainDB = DatabaseHandler()
    mainDB.settup_db(db_name='mainDB.db')
    mainDB.setup_db_table
    '''

    while True:
        print("Main Menu")
        print("1. Show hours per subject")
        print("2. Show weekly hours studied")
        print("3. Exit")

        choice = input("Enter your choice: ")
        

        if choice == '1':
            menu_opt1(excelCSV_raw.dataframe)
        elif choice == '2':
            menu_opt2()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.\n")
        
def menu_opt1(dataframe):
    print()
    hours_per_subject.main(dataframe)
    print("Returning to main menu...\n")

def menu_opt2():
    print()
    print("Performing Task Two...")
    # Your code for task two here
    print("Task Two Completed!\n")


if __name__ == "__main__":
    print("\nRunning program\n")

    sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas\Excel')
        # MODULE_pandas_excel_functions.py

    main_menu()



def oldcode():
    # ============= Modules import ==========
        # 
    sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas')
        # MODULE_pandas_basic.py
