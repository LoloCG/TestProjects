# What the script is meant to do with the excel
    # get all sheet names of an excel
    # upload their data into the df_dict (dictionary data)
    # for each sheet:
        # Obtain max kN, and obtain (X/3)*2 its value
        # Take the required kN value index
        # Copy the range from start to the index
        # into a new df with the name of the sheet
            # e.g.: ref-c-90_1_new
    # Paste all the sheet's new df into a new excel with each its name

    # Make graph of complete dataset and from the selected points (from start of mm to mm at max kN)

import os # Used solely to locate the excel in relationship with the path of the script
import pandas as pd

ALL_SHEETS = True

kN_column = "Fuerza (kN)"

def main():
    # Construct the full path to the Excel file and load it
    script_dir = set_dir_path()
    file_path = os.path.join(script_dir, 'TestExcel.xlsx') 

    if ALL_SHEETS:
        excel_file = pd.ExcelFile(file_path)
        sheet_names = excel_file.sheet_names
        print("Sheet names:",sheet_names)
    else:
        sheet_names = select_sheets(file_path,print_sheets = True)

    df_dict = create_main_dfDict(file_path, sheet_names)

    # show_columns(df_dict)

    kN_req = {}

    for sheet, df in df_dict.items():
        max_kN_required_real = get_required_kN(df, kN_column)
        print("required kN in", {sheet}, "=", max_kN_required_real)
        kN_req[sheet] = max_kN_required_real
        
    max_kN_req_sheet = max(kN_req, key=kN_req.get)
    max_kN_req_value = kN_req[max_kN_req_sheet]
    max_kN_req_index = get_index(df_dict[max_kN_req_sheet], kN_column, max_kN_req_value)

    print("max kN req:", max_kN_req_value, ", from:", max_kN_req_sheet, ", with index:", max_kN_req_index)

    df_all = {} # Initialize the dictionary to store extracted dataframes
    
    for sheet, df in df_dict.items():
        print(f"Processing sheet: {sheet}")
        columns_to_extract = df.columns[1:3].tolist() # determines which columns to extract from the DataFrame.
        
        extracted_data = extract_data_from_columns(df ,0 , max_kN_req_index, columns_to_extract) # extracts a portion of the DataFrame df based on specified columns and row indices.
        print("extracted data of ", {sheet}, ":", extracted_data)

        df_all[sheet] = pd.DataFrame(extracted_data) # creates a new DataFrame from the extracted data and assigns it to the dictionary df_all using the sheet name as the key.

    #create_new_excel(script_dir, df_all)

def set_dir_path(): # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return script_dir

def create_main_dfDict(file_path,selected_sheet_names):
    df_dict = pd.read_excel(file_path, sheet_name=selected_sheet_names)
        # ‘pd.read_excel’ function is used to load the Excel file ‘name.xlsx’ into a Pandas DataFrame called ‘df’. 
        # when pd.read_excel is used with sheet_name=None or a list of sheet names, it results in a dictionary of DataFrames instead of a single DataFrame
            # Therefore, you need to iterate through this dictionary to access each DataFrame's colum. 
            # If you pass a list with a single sheet name to the pd.read_excel function, it will still return a dictionary where the single key is the sheet name and the value is the DataFrame. 
                # This happens because the function treats the sheet_name parameter as potentially containing multiple sheet names.
    return df_dict

def select_sheets(file_path, print_sheets):
    excel_file = pd.ExcelFile(file_path)
    
    sheet_names = excel_file.sheet_names
    
    if print_sheets is True:
        for idx, name in enumerate(excel_file.sheet_names): # loop prints each sheet name with its corresponding index, allowing you to see and select them easily.
            print(f"{idx}: {name}")
    
    sheets_to_select = input("Enter which sheet to copy from: ").split(',')
    sheets_to_select = [int(idx.strip()) for idx in sheets_to_select]
    selected_sheet_names = [sheet_names[idx] for idx in sheets_to_select]

    print("--------")
    print("selected sheet:",selected_sheet_names)

    return selected_sheet_names

def get_index(df, column, value):
    index_obtained = df.index[df[column] == value][0]
    return index_obtained

def get_required_kN(df, column): # Returns the kN required (that which is closest) by applying the formula to the column of kN

    max_kN_value = df[column].max() # Obtain the max value of the column of kN and the required value for the graph
    max_kN_required_exact = (max_kN_value*2)/3 # calculates from the formula
    
    # Finds the number closes to the required kN and then the index
    kN_required_real = df[column].iloc[(df[column] - max_kN_required_exact).abs().argsort()[0]]

    return kN_required_real

def show_columns(df_dict):
    for sheet, df in df_dict.items():
            print(f"Sheet: {sheet}",", columns:", list(df.columns))

    # df_dict is a dictionary where each key is a sheet name from an Excel file, and each value is a Pandas DataFrame containing the data from that sheet.
    # The .items() method returns a view object that displays a list of dictionary's key-value tuple pairs.

def extract_data_from_columns(df,start_idx,end_idx,columns):
    extracted_data = df.loc[start_idx:end_idx, columns]
    return extracted_data

def create_new_excel(script_dir,df_all):
    #Construct the full path to the new Excel file
    output_path = os.path.join(script_dir, 'NewExcel.xlsx')
    
    with pd.ExcelWriter(output_path) as writer:
        for sheet_name, df in df_all.items():
            clean_sheet_name = str(sheet_name) + "_new"
            df.to_excel(writer, sheet_name=clean_sheet_name, index=False)
        
        
    #newdf.to_excel(writer, sheet_name=output_sheet_name, index=False)

    # You can also simply use "newdf.to_excel(output_path, index=False)" to not expecify sheet name
    # Using the context manager (with pd.ExcelWriter() as writer) is generally recommended for more complex scenarios, such as writing to multiple sheets or setting more options
    
main()



'''
def unused_code():
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

'''