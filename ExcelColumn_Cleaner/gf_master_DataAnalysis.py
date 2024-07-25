# What the script is meant to do with the excel
    # get all data from an excel and unloads into dataframe "df_dict", separating each sheet. 
    # Searches with a for loop important values in df_dict
        # the max kN of all series, along their mm and sheets
        # saves the one which has highest mm at the max kN
        # checks if a series starts below a threshold of kN, and if so, saves into dictionary "below_threshold_data"
    # Uses the index of the highest mm and adds 1/3 values for extra graph path
    # Another for loop extracts the value into a new dataframe "df_clean"
        # gets the start idx and end idx from each series
            # if the series had values below threshold, it takes from the closest to it, and substracts its mm to all its mm of the series
    # Creates the excel unloading the data from df_clean into different sheets, and creates the graph

import pandas as pd
import os
import numpy as np

kN_column = "Fuerza (kN)"
mm_column = "Carrera (mm)"  
min_threshold_kN_value = 0.5 
    # in TestExcel1, REF-C-90-1 starts at 0,0924
    # in TestExcel2, REF-C-90-1 starts at 0,0924; # TODO: test with multiple sub threshold sheets

script_dir = os.path.dirname(os.path.abspath(__file__))
inputData_dir = os.path.join(script_dir, 'InputData') # The folder where input excels are located
output_path = os.path.join(script_dir, 'NewExcel2.xlsx') # TODO: make more dynamic naming of output file

def main():
    input_excels = show_folder_files(inputData_dir) # Prints the files in input folder. # TODO: there is no error handling

    chosen_file = userInput_excel_select(input_excels) # asks user to select file from folder

    file_path = os.path.join(inputData_dir, chosen_file) 
    df_dict = load_df_dictionary(file_path)
    
    # Sets the variables to save the values from the loop
    max_mm_value = -1 
    max_mm_sheet = -1
    below_threshold_data = []  # Dict to store all data regarding series below the mm threshold (sheet, value and index)
        
    for sheet, df in df_dict.items(): # goes through each sheet, reading all important values and saving them in memory
        print()
        print(f"reading {sheet}...")
        
        mm_of_kN = get_mm_values(df) 

        if mm_of_kN > max_mm_value: # Saves the 'max mm' that it encounters, along the sheet that it is found.
            max_mm_value = mm_of_kN 
            max_mm_sheet = sheet
        
        start_kN_value = df.at[0, kN_column] # Obtains the first value in kN column
        
        if start_kN_value < min_threshold_kN_value: # If the data starts below the threshold, saves location into dictionary "below_threshold_data"
            below_threshold_data = get_closest_to_threshold(sheet, df, below_threshold_data)             

    print()
    print("max mm = ", max_mm_value, " in ", max_mm_sheet)
    # ===========================
    
    idx_closest_req_mm = get_req_mm_idx(df_dict, max_mm_sheet, max_mm_value) # Obtains index of mm that exists in the data, that is closest to what is required

    df_clean = {}

    for sheet, df in df_dict.items(): # Uses the start and end to extract the data and place in a new df (df_clean)
        print(f"extracting from {sheet}")
        print()
        idx_start, idx_end = get_idx_start_end(sheet, idx_closest_req_mm, below_threshold_data) # (sheet, sheet_below_threshold, first_idx_above_threshold, idx_closest_req_mm)

        extracted_data = extract_data_from_df(df, idx_start, idx_end)
        extracted_data = remove_below_threshold_values(sheet, below_threshold_data, extracted_data)

        df_clean[sheet] = pd.DataFrame(extracted_data) # creates a new DataFrame from the extracted data and assigns it to the dictionary df_clean using the sheet name as the key.
        
    # Combine all unique X values from all series
    combined_X = np.array([]) # Initializes an empty NumPy array to store unique X values
        # TODO: why use a np.array?

    df_averages = create_df_avg(combined_X, df_clean)

    # Add the averages DataFrame to the dictionary with a new key
    df_clean['Averages'] = df_averages

    create_output_excel(output_path, df_clean)
    print("...")
    print("new excel created")

    print("opening excel...")
    os.startfile(output_path) # open the excel file
    print("...")

    eliminate_input_file(output_path)

def show_folder_files(inputData_dir): # Prints all files in the input folder, and returns it

    input_excels = os.listdir(inputData_dir)

    print("Files in the folder:")
    for index, file in enumerate(input_excels):
        print(f"{index + 1}: {file}")

    return input_excels

def userInput_excel_select(input_excels):
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
    return chosen_file
            
def load_df_dictionary(file_path): # Uloads the data from the excel files into dataframe "df_dict"
    excel_file = pd.ExcelFile(file_path) # Opens the excel file (???)
    sheet_names = excel_file.sheet_names # Obtains the sheet names of the file
    print("Sheet names:", sheet_names)
    df_dict = pd.read_excel(file_path, sheet_name=sheet_names) # Loads the excel file to the df_dict dataframe, with all its different sheets
    return df_dict

def get_mm_values(df):
    max_kN_value = df[kN_column].max()  # Searches the max value of kN
    index_max_kN = df.index[df[kN_column] == max_kN_value][0] # obtains the index of max kN value found
    
    mm_of_kN = df.at[index_max_kN, mm_column] # Obtains the mm of that max kN value
    print("max kN =", max_kN_value, ", index =", index_max_kN, ", mm =", mm_of_kN)
    
    return mm_of_kN

def get_closest_to_threshold(sheet, df, below_threshold_data):
    sheet_below_threshold = sheet
    first_val_above_threshold = df[df[kN_column] > min_threshold_kN_value][kN_column].iloc[0] # obtain the value that is closest to the threshold
    first_idx_above_threshold = df.index[df[kN_column] == first_val_above_threshold][0] # obtain the index of that value
    first_mm_above_threshold = df.at[first_idx_above_threshold, mm_column]

    below_threshold_data.append({
        "below_threshold_sheet": sheet,
        "first_val_above_threshold": first_val_above_threshold,
        "first_idx_above_threshold": first_idx_above_threshold,
        "first_mm_above_threshold": first_mm_above_threshold
    })

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
    print("...")
    return idx_closest_req_mm
    #================================================
        
def get_idx_start_end(sheet, idx_closest_req_mm, below_threshold_data):
    for data in below_threshold_data:
        if data["below_threshold_sheet"] == sheet:
            first_idx_above_threshold = data["first_idx_above_threshold"]
            
            idx_start = first_idx_above_threshold
            idx_end = idx_closest_req_mm + first_idx_above_threshold

            return idx_start, idx_end

    idx_start = 0
    idx_end = idx_closest_req_mm

    return idx_start, idx_end

def extract_data_from_df(df, idx_start, idx_end): # extracts the data from df_dict, choosing the columns and start & ending
    columns_to_extract = df.columns[1:3].tolist() # determines which columns to extract from the DataFrame.
    print("starting on:", idx_start)

    extracted_data = df.loc[idx_start:idx_end, columns_to_extract] # extracts a portion of the DataFrame df based on specified columns and row indices.

    return extracted_data

def remove_below_threshold_values(sheet, below_threshold_data, extracted_data):
    for data in below_threshold_data:
        if data["below_threshold_sheet"] == sheet:
            first_mm_above_threshold = data["first_mm_above_threshold"]

            extracted_data[mm_column] = extracted_data[mm_column] - first_mm_above_threshold
            print(first_mm_above_threshold," has been removed from mm")

            return extracted_data
        else:
            return extracted_data

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

def unused_code():
    '''  
    print()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    inputData_dir = os.path.join(script_dir, 'InputData')

    input_excels = os.listdir(inputData_dir)


    first_idx_above_threshold = None
    first_val_above_threshold = None
    sheet_below_threshold = None

    for sheet, df in df_dict.items():
        start_kN_value = df.at[0, kN_column] # Obtains the first value in kN column
        
        if start_kN_value < min_threshold_kN_value:
            sheet_below_threshold = sheet
            first_val_above_threshold = df[df[kN_column] > min_threshold_kN_value][kN_column].iloc[0] # obtain the value that is closest to the threshold
            first_idx_above_threshold = df.index[df[kN_column] == first_val_above_threshold][0] # obtain the index of that value
            
            print("first value > threshold:", first_val_above_threshold, ", idx = ", first_idx_above_threshold)

    for sheet, df in df_dict.items():

        if sheet == below_threshold_data[below_threshold_sheet]: 
            idx_start = below_threshold_data[first_idx_above_threshold]
            idx_end = idx_closest_req_mm + below_threshold_data[first_idx_above_threshold]
        else:
            idx_start = 0
            idx_end = idx_closest_req_mm

        with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
            for sheet_name, df in df_all.items():
                clean_sheet_name = f"{sheet_name}_new"
                df.to_excel(writer, sheet_name=clean_sheet_name, index=False)
    
        with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
            for sheet_name, df in df_all.items():
                clean_sheet_name = str(sheet_name) + "_new"
                df.to_excel(writer, sheet_name=clean_sheet_name, index=False)        
        #newdf.to_excel(writer, sheet_name=output_sheet_name, index=False)

        # You can also simply use "newdf.to_excel(output_path, index=False)" to not expecify sheet name
        # Using the context manager (with pd.ExcelWriter() as writer) is generally recommended for more complex scenarios, such as writing to multiple sheets or setting more options

    def unused_code():

        # Re-open the Excel file in append mode
        with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
            workbook = writer.book

            # Create a new worksheet to add the chart
            worksheet = workbook.add_worksheet('Chart')

            chart = workbook.add_chart({'type': 'line'})  # Create a line chart

            # Add series to the chart using the retrieved worksheet names and dynamic ranges
            for sheet_name, df in df_all.items():
                last_row = len(df)  # Use len(df) to get the last row dynamically 
                    # can also be used something such as: 
                    # last_row = max_kN_req_index + 1  # +1 because Excel ranges are inclusive
                chart.add_series({
                    'name': f'{sheet_name} Data',
                    'categories': f'={sheet_name}!$A$2:$A${last_row}',
                    'values': f'={sheet_name}!$B$2:$B${last_row}',
                })

            worksheet.insert_chart('A1', chart)

            writer._save()

            workbook.close()

        # Print all column names so you can see how they are labeled.
        print("named columns in dataset:",df.columns)
        print("----------")

        # idxmax method to get the index of the maximum value and then use that index to locate the adjacent column's value.
        max_kN_index = df[kN_column].idxmax()  # Get the index of the max value
        mm_of_max_kN = df.at[max_kN_index, 'Carrera (mm)']
            # '.at' is a pandas accessor method used to access a single value for a row/column label pair.
            # The .iloc method in pandas is used for integer-location based indexing and selection by position. It allows you to access a specific row or column in a DataFrame using its integer index

        # Finds the number closes to the required kN to show for graph
        max_kN_required_real = df[kN_column].iloc[(df[kN_column] - max_kN_required_exact).abs().argsort()[0]]
        # Find the Index of the Target Value:
        index_of_target = df.index[df[kN_column] == max_kN_required_real][0]
        # Retrieve the Adjacent Value:
        mm_of_target_kN = df.at[index_of_target, 'Carrera (mm)']

        print("max kN in data =", max_kN_value)
        print("mm of max kN =", mm_of_max_kN)
        print("----------")
        print("kN closes to '(x*2)/3':", max_kN_required_real)
        print("mm closes to '(x*2)/3':", mm_of_target_kN)

        # Extract data from the first column to the required kN
        kN_required_range = df.iloc[0:index_of_target] #[index_of_target:len(df)]

        kN_required_df = pd.DataFrame(kN_required_range)

        set_dir_path = set_path()
        output_path = os.path.join(script_dir, 'cleaned_data.xlsx')
        kN_required_df.to_excel(output_path, index=False)


    def extract_data_from_column(df,start_idx,end_idx,column): # Extracts all the data from the specified start and ending indexes of the specified column
        extracted_data = df.iloc[start_idx:end_idx, [column]]


    if start_value is None:
        start_idx = 0
    else:
        start_idx = df[df[column_name] == start_value].index[0] # searches for the row where the value in column_name matches start_value. It then retrieves the index of this row.
            # df[df[column_name] == start_value] creates a boolean mask where the condition is true.
            # .index[0] fetches the first index where this condition is met.

    if end_value is None:
        end_idx = len(df) # end_idx is set to the length of the DataFrame, which is len(df).
    else:
        end_idx = df[df[column_name] == end_value].index[0] + 1  # +1 to include the end value. 
            # searches for the row where the value in column_name matches end_value. 
            # It then retrieves the index of this row.

    extracted_data = df.iloc[start_idx:end_idx] # extracts the data from the DataFrame within the specified index range
        # it uses not only the column from which the index is specified, but all the other columns as well.
    '''

    '''
    # Create or Load the Cleaned DataFrame
    cleaned_df = pd.DataFrame() # creates new dataframe named 'cleaned_df' where it stores the new data

    # Add the Values to the Cleaned DataFrame: 

    # Assign values to the cleaned DataFrame
    cleaned_df.at[0, 'kN_values'] = max_kN_value
    cleaned_df.at[0, 'mm_values'] = mm_of_max_kN
    cleaned_df.at[1, 'kN_values'] = max_kN_required_real
    cleaned_df.at[1, 'mm_values'] = mm_of_target_kN

    # Construct the full path to the new Excel file
    output_path = os.path.join(script_dir, 'cleaned_data.xlsx')

    # Save the new DataFrame to a cleaned Excel fileS
    cleaned_df.to_excel(output_path, index=False)
        # to_excel specifies the path or ExcelWriter object where the DataFrame should be written.
        # then is the name of the sheet in the Excel file where the DataFrame should be written. (str, default 'Sheet1')
        # When index=False is specified, the row indices are not written to the Excel file. 
            # This means that only the data and column headers are written, making the file cleaner if the index is not needed
        # there are many other parameters that can be used. (merging cells, how to represent infinity, the encoding, engine to use for writing , starting row and column...)


    # Merge each original series DataFrame with the final DataFrame
    for series_name, df in df_clean.items():
        df_final = pd.merge(df_final, df, on=mm_column, how='outer', suffixes=('', f'_{series_name}'))

    # Sort the final DataFrame by the common column
    df_final = df_final.sort_values(by=mm_column).reset_index(drop=True)

    print()
    # ============================================

    print(df_final)
    '''

    print("test")

    chart.add_series({
        'name':         f'{sheet_name} Data',
        'categories':   f'={sheet_name}!$B$2:$A${last_row}',
        'values':       f'={sheet_name}!$B$2:$B${last_row}',
    })

    #writer.save()

    # Create a chart object.
    chart = workbook.add_chart({"type": "line"})

    for sheet_name, df in df_clean.items():
        print(f"Plotting data from {sheet_name}")
        last_row = len(df) + 1
        
        chart.add_series({
            'name':         f'{sheet_name} Data',
            'categories':   ["{sheet_name}", 1, 1, last_row, 1],
            'values':       ["{sheet_name}", 1, 0, last_row, 0],
        })
    
    chart.set_legend({'position': 'none'})


    for sheet_name, df in df_clean.items():
        print(f"Plotting data from {sheet_name}")
        last_row = len(df) + 1

        print("str:",str({sheet_name})) # ='{''REF-C-90-1''}'!$B$2:$B$533

        new_sheetname = append(str({sheet_name})&"_new")
        print("append:",new_sheetname) # 

        chart.add_series({
            'name':         f'{sheet_name} Data',
            'categories':   [str({sheet_name})&"_new", 1, 0, last_row, 0],
            'values':       [str({sheet_name})&"_new", 1, 1, last_row, 1],
        })

    # Configure the chart axes.
    chart.set_x_axis({'name': 'mm', 'position_axis': 'on_tick'})
    chart.set_y_axis({'name': 'kN', 'major_gridlines': {'visible': False}})
    
    chart.set_legend({'position': 'top'})

    worksheet.insert_chart(1, 3, chart)
    #worksheet.insert_chart('D2', chart)    '''

    #writer.close()
    #writer.save()