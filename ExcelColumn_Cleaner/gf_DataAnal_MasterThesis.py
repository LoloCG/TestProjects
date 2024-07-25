import pandas as pd
import os
import numpy as np

# ============================== MANUAL PARAMETERS ==============================
NOT_CREATE_EXCEL = False
AUTO_DETECT_THRESHOLD = False

    # !!!!!!!!!!!!!
MANUAL_THRESHOLD = float('0.9') # This value was used for the test excel. Change accordingly
    # !!!!!!!!!!!!!

kN_column = "Fuerza (kN)" # Make sure both columns are called like this
mm_column = "Carrera (mm)"  

inputData_dir = os.path.join(script_dir, 'Input_folder') 
    # Otherwise use this to select the folder:
    # inputData_dir = r'C:\Users\Lolo\Desktop\Graph Patty\Semi-Raw' # Folder containing the excel files

# ============================== GLOBAL VARIABLES ==============================
script_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    global MANUAL_THRESHOLD

    print("loading files...")

    file_path, chosen_file, selected_sheets = userInput_excel_select(inputData_dir) 
    
    df_dict = load_df_dictionary(file_path, selected_sheets)

    # Sets the variables to save the values from the loop
    max_mm_value = -1 
    max_mm_sheet = -1
    below_threshold_data = {}  # Dict to store all data regarding series below the mm threshold (sheet, value and index)
        
    for sheet, df in df_dict.items(): # goes through each sheet, reading all important values and saving them in memory
        print()
        print(f"reading {sheet}...")

        mm_of_kN = get_mm_values(df) 

        if mm_of_kN > max_mm_value: # Saves the 'max mm' that it encounters, along the sheet that it is found.
            max_mm_value = mm_of_kN 
            max_mm_sheet = sheet

        start_kN_value = df.at[0, kN_column] # Obtains the first value in kN column

        if not AUTO_DETECT_THRESHOLD:
            min_threshold_kN_value = MANUAL_THRESHOLD
        else: 
            return

        if start_kN_value < min_threshold_kN_value: # If the data starts below the threshold, saves location into dictionary "below_threshold_data"
            below_threshold_data = get_closest_to_threshold(sheet, df, below_threshold_data, min_threshold_kN_value)             

    print()
    print("max mm = ", max_mm_value, " in ", max_mm_sheet)

    idx_closest_req_mm = get_req_mm_idx(df_dict, max_mm_sheet, max_mm_value) # Obtains index of mm that exists in the data, that is closest to what is required

    '''
    if not AUTO_DETECT_THRESHOLD:
        print(f"Manual threshold is set to", MANUAL_THRESHOLD)
        user_input = input(f"Press 'N' to change it: ").strip().upper()
        if user_input == 'N':
            MANUAL_THRESHOLD = input(f"Enter new threshold: ")
            print(f"New Threshold set to {MANUAL_THRESHOLD}.")
            print()
    else:
        print("Autodetection of threshold from data is not incorporated yet.")
    '''
    df_clean = {}
    for sheet, df in df_dict.items(): # Uses the start and end to extract the data and place in a new df (df_clean)
        print(f"extracting from {sheet}")
        
        idx_start, idx_end = get_idx_start_end(sheet, idx_closest_req_mm, below_threshold_data) # (sheet, sheet_below_threshold, first_idx_above_threshold, idx_closest_req_mm)

        extracted_data = extract_data_from_df(df, idx_start, idx_end)
        extracted_data = remove_below_threshold_values(sheet, below_threshold_data, extracted_data)

        df_clean[sheet] = pd.DataFrame(extracted_data) # creates a new DataFrame from the extracted data and assigns it to the dictionary df_clean using the sheet name as the key.
        print()

    # Combine all unique X values from all series
    combined_X = np.array([]) # Initializes an empty NumPy array to store unique X values
        # TODO: why use a np.array?

    df_averages = create_df_avg(combined_X, df_clean)

    # Add the averages DataFrame to the dictionary with a new key
    df_clean['Averages'] = df_averages
    print()
    
    output_name = input(f"Enter the name of new Excel file (leave blank for {chosen_file}): ")

    if output_name.strip() == "":  
        output_filename = chosen_file.rsplit('.', 1)[0] + '.xlsx'
    else:
        output_filename = chosen_file + '.xlsx'
    
    print(f"filename: {output_filename}")
    
    output_path = os.path.join(script_dir, output_filename)  # Creates the full output path
    
    if not NOT_CREATE_EXCEL:
        create_output_excel(output_path, df_clean)

        print()
        print("new excel created")

        print("opening excel...")
        os.startfile(output_path) # open the excel file
        print("...")

        eliminate_input_file(output_path)

    else:
        print("debug mode, not creating excel")

def show_folder_files(inputData_dir): # Prints all files in the input folder, and returns it
    
    input_excels = os.listdir(inputData_dir)
    print()
    print("Files in the folder:")
    for index, file in enumerate(input_excels):
        print(f"{index + 1}: {file}")

    return input_excels

def userInput_excel_select(inputData_dir):
    input_excels = show_folder_files(inputData_dir)

    while True:
        try:
            choice = int(input(f"Enter the number of the file you want to open (1-{len(input_excels)}): "))
            if 1 <= choice <= len(input_excels):
                chosen_file = input_excels[choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(input_excels)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"chosen file: {chosen_file}")
    print()
    
    file_path = os.path.join(inputData_dir, chosen_file) 

    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names

    for index, sheet in enumerate(sheet_names):
        print(f"{index + 1}: {sheet}")
    
    user_input = input("Enter the sheet numbers to load (comma-separated, or blank for all): ")

    # Parse user input
    if user_input.strip() == "":
        selected_sheets = sheet_names
    else:
        selected_indices = [int(i) - 1 for i in user_input.split(',')]
        selected_sheets = [sheet_names[i] for i in selected_indices]

    print(f"selected sheets: {str(selected_sheets)}")
    print()

    return file_path, chosen_file, selected_sheets
            
def load_df_dictionary(file_path, selected_sheets): # Uloads the data from the excel files into dataframe "df_dict"
    df_dict = {}
    for sheet in selected_sheets:
        print(f"loading {sheet} into df_dict")
        df_dict[sheet] = pd.read_excel(file_path, sheet_name=sheet)
    return df_dict

def get_mm_values(df):
    max_kN_value = df[kN_column].max()  # Searches the max value of kN
    index_max_kN = df.index[df[kN_column] == max_kN_value][0] # obtains the index of max kN value found
    
    mm_of_kN = df.at[index_max_kN, mm_column] # Obtains the mm of that max kN value
    print("max kN =", max_kN_value, ", index =", index_max_kN, ", mm =", mm_of_kN)
    
    return mm_of_kN

def get_closest_to_threshold(sheet, df, below_threshold_data, min_threshold_kN_value):
    above_threshold_df = df[df[kN_column] > min_threshold_kN_value]
    
    if above_threshold_df.empty:
        print(f"{sheet} does not have any values above the threshold.")
        
    else:
        #sheet_below_threshold = sheet
        first_val_above_threshold = df[df[kN_column] > min_threshold_kN_value][kN_column].iloc[0] # obtain the value that is closest to the threshold
        first_idx_above_threshold = df.index[df[kN_column] == first_val_above_threshold][0] # obtain the index of that value
        first_mm_above_threshold = df.at[first_idx_above_threshold, mm_column]

        below_threshold_data[sheet] = {
            "first_val_above_threshold": first_val_above_threshold,
            "first_idx_above_threshold": first_idx_above_threshold,
            "first_mm_above_threshold": first_mm_above_threshold
        }

        print(f"{sheet} starts lower than threshold.",
            "First above threshold:", first_val_above_threshold, 
            ", idx = ", first_idx_above_threshold)

    return below_threshold_data

def get_req_mm_idx(df_dict, max_mm_sheet, max_mm_value): # Finds the index of mm + 1/3 from the sheet that has higher mm

    #===============================================
    # Obtains the sheet with max_mm_value and creates a df. Then obtains the required, its closest, and the index.
        #  TODO: is creating a new df necessary?
    df_max_mm = df_dict[max_mm_sheet]   # Creates dataframe "df_max_mm", with only the sheet that contains the max_mm_value

    req_mm_val = max_mm_value + (max_mm_value/3)

    closest_req_mm = df_max_mm[mm_column].iloc[(df_max_mm[mm_column] - req_mm_val).abs().argsort()[0]]
    idx_closest_req_mm = df_max_mm.index[df_max_mm[mm_column] == closest_req_mm][0]

    print("req_mm_val =", req_mm_val, ", closest = ", closest_req_mm, "at index:", idx_closest_req_mm)
    print()
    return idx_closest_req_mm
    #================================================
        
def get_idx_start_end(sheet, idx_closest_req_mm, below_threshold_data):
    if sheet in below_threshold_data:
        first_idx_above_threshold = below_threshold_data[sheet]["first_idx_above_threshold"]
        
        idx_start = first_idx_above_threshold
        idx_end = idx_closest_req_mm + first_idx_above_threshold
    else:
        idx_start = 0
        idx_end = idx_closest_req_mm

    return idx_start, idx_end
    # TODO: remove unused code
    '''
    for data in below_threshold_data:
        if data["below_threshold_sheet"] == sheet:
            first_idx_above_threshold = data["first_idx_above_threshold"]
            
            idx_start = first_idx_above_threshold
            idx_end = idx_closest_req_mm + first_idx_above_threshold

            return idx_start, idx_end

    idx_start = 0
    idx_end = idx_closest_req_mm

    return idx_start, idx_end
    '''

def extract_data_from_df(df, idx_start, idx_end): # extracts the data from df_dict, choosing the columns and start & ending
    columns_to_extract = df.columns[1:3].tolist() # determines which columns to extract from the DataFrame.
    print("starting on:", idx_start)

    extracted_data = df.loc[idx_start:idx_end, columns_to_extract] # extracts a portion of the DataFrame df based on specified columns and row indices.

    return extracted_data

def remove_below_threshold_values(sheet, below_threshold_data, extracted_data):
    if sheet in below_threshold_data:
        first_mm_above_threshold = below_threshold_data[sheet]["first_mm_above_threshold"]
        extracted_data[mm_column] = extracted_data[mm_column] - first_mm_above_threshold
        print(first_mm_above_threshold, "has been removed from mm in", sheet)

    return extracted_data
    # TODO: remove unused code
    '''
    for data in below_threshold_data:
        if data["below_threshold_sheet"] == sheet:
            first_mm_above_threshold = data["first_mm_above_threshold"]
            sheet = data["below_threshold_sheet"]

            extracted_data[mm_column] = extracted_data[mm_column] - first_mm_above_threshold
            print(first_mm_above_threshold,"has been removed from mm in",sheet)

            return extracted_data
        else:
            return extracted_data
    '''

def create_df_avg(combined_X, df_clean):
    for series_name, df in df_clean.items():
        print("Combining mm from",series_name)
        print("length of data:", len(df))
        combined_X = np.union1d(combined_X, df[mm_column]) # Combine and sort unique X values
            # Each np.union1d call merges and sorts the unique X values, and if there are many unique X values across all series, the combined set will be larger.
        
    # Create a combined DataFrame with all unique X values
    df_combined = pd.DataFrame(combined_X, columns=[mm_column])
    df_combined = df_combined.sort_values(by=mm_column).reset_index(drop=True)

    # Interpolate Y values for each series at the combined X values
    for series_name, df in df_clean.items():
        df_combined[f'{kN_column}_{series_name}'] = np.interp(df_combined[mm_column], df[mm_column], df[kN_column])

    # Calculate the average of Y values
    combined_kN_columns = [col for col in df_combined.columns if col.startswith(f'{kN_column}_')]
    df_combined[f'{kN_column}_avg'] = df_combined[combined_kN_columns].mean(axis=1)

    # Calculate the average of Y values
    combined_kN_columns = [col for col in df_combined.columns if col.startswith(f'{kN_column}_')]
    df_combined[f'{kN_column}_avg'] = df_combined[combined_kN_columns].mean(axis=1)

    # Result: Only the averages as a DataFrame
    df_averages = df_combined[[f'{kN_column}_avg', mm_column]]
    
    return df_averages

def create_output_excel(output_path, df_clean):
    # Retrieve the last value of "Carrera (mm)" in the "Averages" DataFrame
    last_value_mm = df_clean['Averages'][mm_column].iloc[-1]
    last_value_mm = np.ceil(last_value_mm)

    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        workbook = writer.book

        for sheet_name, df in df_clean.items():
            print(f"Adding data from sheet: {sheet_name}")
            clean_sheet_name = f"{sheet_name}"
            df.to_excel(writer, sheet_name=clean_sheet_name, index=False)  
        
        # Create an empty df that will be used to create the chart
        empty_df = pd.DataFrame() 
        empty_df.to_excel(writer, sheet_name="Chart", index=False)
        worksheet = writer.sheets['Chart']

        print("...")
        print("Creating chart...")
        
        chart = workbook.add_chart({'type': 'scatter'})
        
        for sheet_name, df in df_clean.items():
            print(f"Plotting data from {sheet_name}")

            last_row = len(df)

            # Determine the line style
            line_style = {'width': 2}
            if sheet_name == "Averages": # Change style for Averages
                line_style['dash_type'] = 'dash'
                line_style['color'] = 'red' 
                line_style['width'] = 3

            chart.add_series({
                'name':         f'{sheet_name}',
                'categories':   [f"{sheet_name}", 1, 1, last_row, 1],
                'values':       [f"{sheet_name}", 1, 0, last_row, 0],
                'marker':       {'type': 'none'},
                'line':         line_style,
                'smooth':       True
            })

        chart.set_x_axis({
            'name': 'Carrera (mm)', 
            'num_format': '0.00',  # Set number format to display 2 decimal places
            'position_axis': 'on_tick', # Positions the axis on the tick marks.
            'major_gridlines': {'visible': True},
            'min': 0,
            'max': last_value_mm,
            'interval_unit': 50,
            'interval_tick': 100 
            })
        
        print("max value set as", last_value_mm)
        
        chart.set_y_axis({
            'name': 'Fuerza (kN)',
            'num_format': '0.0',
            'major_gridlines': {'visible': True},
            })
        
        chart.set_legend({'position': 'bottom'})
        chart.set_title({'name': 'kN vs mm Carrera'})  # TODO: make more dynamic, based on the data that is processed (eg. REF-C-90), etc
        chart.set_style(37)

        worksheet.insert_chart(0, 0, chart)

def eliminate_input_file(output_path): # Asks user whether to eliminate file from output_path
    if os.path.exists(output_path):
        user_input = input(f"Eliminate excel? (Y/N): ").strip().upper()
        if user_input == 'Y':
            os.remove(output_path)
            print(f"File has been removed.")
        else:
            print(f"File was not removed.")
    else:
        print(f"File does not exist.")

main()