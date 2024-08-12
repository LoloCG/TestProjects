import sys
from modules import ExcelDataExtract
import hours_per_subject

def main_menu():
    print("Reading database...")
    chosen_file = '3º FarmNutr TDL_Log.csv'
    sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas\Excel')

    excelCSV_raw = ExcelDataExtract()
    excelCSV_raw.csv_to_dataframe(chosen_file)

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
    main_menu()