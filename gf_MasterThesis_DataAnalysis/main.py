import gf_DataAnal_MasterThesis

xlsObjInfo = None

def main():
    option_list = [
        'Graph Hydraulic Press results',
        'Re-Do same set',
        'Create avg of avg'
    ]
    main_menu_dialog(option_list)

def main_menu_dialog(option_list):
    while True:
        
        print("Main Menu")
        for n in range(len(option_list)): 
            print(f"{n+1}. {option_list[n]}")
        
        exit_num = len(option_list) + 1
        print(f"{exit_num}. Exit")

        choice = int(input("Enter your choice: "))
        #print(f"DEBUG: Choice = {choice}, {option_list[choice - 1]}") 

        if choice == 1:
            menu_opt1(False)
        elif choice == 2:
            menu_opt1(True)
        elif choice == exit_num:
            print("Exiting the program.")
            return
        else:
            print("Invalid choice, please try again.\n")

def menu_opt1(reDoGraph):
    print()
    xlsObjInfo = gf_DataAnal_MasterThesis.main(reDoGraph)

if __name__ == "__main__":
    print("\nRunning program\n")
    main()

