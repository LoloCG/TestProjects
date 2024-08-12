import pandas as pd
import os
import numpy as np
import sys

# ============================== MANUAL PARAMETERS ==============================
NOT_CREATE_EXCEL = False
AUTO_DETECT_THRESHOLD = False
INPUT_DATA_IN_SCRIPT_DIR = True

# !!!!!!!!!!!!!
MANUAL_THRESHOLD = float('0.9') # This value was used for the test excel. Change accordingly

outputData_dir = r''
# ============================== GLOBAL VARIABLES ==============================

kN_column = "Fuerza (kN)" # Make sure both columns are called like this
mm_column = "Carrera (mm)"  

def main():
    global MANUAL_THRESHOLD

    excel_load = excel_mod.ExcelDataExtract()
    excel_load.get_folder_excel_files(inputData_dir)
    excel_load.select_excelFile_fromFolder()
    excel_load.select_excelSheets_fromFile()
    excel_load.load_excel_to_dataframe_dict()

    hydraulicValues = HydraulicAnalysis(dataframe=excel_load.dataframe)
    hydraulicValues.get_max_kN_mm()
    hydraulicValues.get_start_end_idx_val()
    new_dict_df = hydraulicValues.extract_data_from_df()

    df_averages = create_df_avg(new_dict_df)
    new_dict_df['Averages'] = df_averages
    

    old_file = excel_load.chosen_file
    output_name = input(f"\nEnter the name of new Excel file (leave blank for {old_file}): ")
    
    if output_name.strip() == "":  
        output_filename = old_file.rsplit('.', 1)[0] + '.xlsx'
    else:
        output_filename = old_file + '.xlsx'
    
    print(f"filename: {output_filename}\n")
    output_path = os.path.join(script_dir, output_filename)  # Creates the full output path
    
    if not NOT_CREATE_EXCEL:
        create_output_excel(output_path, new_dict_df)

        print()
        print("new excel created")

        print("opening excel...")
        os.startfile(output_path) # open the excel file
        print("...")

        eliminate_input_file(output_path)

    else:
        print("debug mode, not creating excel")

def create_df_avg(df_clean):
    # Combine all unique X values from all series
    combined_X = np.array([]) # Initializes an empty NumPy array to store unique X values

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

class HydraulicAnalysis:
    def __init__(self, dataframe: pd.DataFrame, sheet_name=None):
        self.dataframe = dataframe
        
        if isinstance(self.dataframe, dict):
            print("Dataframe is dictionary type\n")
            # For each sheet name, create an empty dictionary in self.results
            # This will store what is of importance by sheet, then by key (e.g.: max_kN), then the values
            self.hydrvalues = {sheet_name: {} for sheet_name in dataframe.keys()}

            self.maxmm_of_maxkN = (-1000,None) # Tuple that stores the highest 'mm of max kN' [0] and the sheet [1] where it is found.

            self.idx_start_end_dict = {sheet_name: {} for sheet_name in dataframe.keys()}

        else:
            self.sheet_name = sheet_name
            self.max_kN = None
            self.index_max_kN = None
            self.mm_of_max_kN = None

    def get_max_kN_mm(self):
        if isinstance(self.dataframe, dict):
            for sheet, df in self.dataframe.items():
                print(f"Obtaining max values for sheet {sheet}...")
                max_kN = df[kN_column].max()
                index_max_kN = df.index[df[kN_column] == max_kN][0] # obtains the index of max kN value found
                mm_of_kN = df.at[index_max_kN, mm_column] # Obtains the mm of that max kN value
                                        
                # Add the calculated value to the results dictionary for the corresponding sheet
                self.hydrvalues[sheet]['max_kN'] = max_kN
                self.hydrvalues[sheet]['mm_of_kN'] = mm_of_kN
            
            print()
            self.__get_dfdict_max_mm()

        else:
            self.max_kN = self.dataframe[kN_column].max()
            self.index_max_kN = self.dataframe.index[self.dataframe[kN_column] == self.max_kN][0] # obtains the index of max kN value found
            self.mm_of_max_kN = self.dataframe.at[index_max_kN, mm_column]

    def __get_dfdict_max_mm(self):
        for key, inner_dict in self.hydrvalues.items():
            if inner_dict['mm_of_kN'] > self.maxmm_of_maxkN[0]:
                self.maxmm_of_maxkN = (inner_dict['mm_of_kN'], key) # Tuple structure.

        print(f"Highest mm of max kN value is {self.maxmm_of_maxkN[0]}, found in '{self.maxmm_of_maxkN[1]}'.")
        
    def __get_idx_req_mm(self): # Finds the index of mm + 1/3 from the sheet that has higher mm
        if isinstance(self.dataframe, dict):
            df = self.dataframe[self.maxmm_of_maxkN[1]] # The dataframe that contains the max mm

            req_mm_val = self.maxmm_of_maxkN[0] + (self.maxmm_of_maxkN[0]/3)

            closest_req_mm = df[mm_column].iloc[(df[mm_column] - req_mm_val).abs().argsort()[0]]
            idx_req_mm = df.index[df[mm_column] == closest_req_mm][0]

            print(f"Closest req mm: {closest_req_mm}, with idx: {idx_req_mm}")
            return idx_req_mm
        else:
            print("TODO: function 'get_req_mm() in HydraulicAnalysis class is not yet for single dataframes")
            return None
        #================================================
 
    def get_closest_to_threshold(self, sheet = None):
        if isinstance(self.dataframe, dict):
            df = self.dataframe[sheet]

            start_kN_value = df[kN_column].at[0]
            all_below_threshold = df[kN_column] > MANUAL_THRESHOLD
                
            if all_below_threshold.empty:
                print(f"!!!\n{sheet} does not have any values above the threshold.")
                
                return None

            # If the sheet has values below threshold, locate the first one that is equal or greater 
            elif start_kN_value < MANUAL_THRESHOLD: 
                print(f"Starting kN value of {sheet} ({start_kN_value}) is below the threshold ({MANUAL_THRESHOLD})")

                first_val_above_threshold = df[df[kN_column] > MANUAL_THRESHOLD][kN_column].iloc[0] # obtain the value that is closest to the threshold
                first_idx_above_threshold = df.index[df[kN_column] == first_val_above_threshold][0] # obtain the index of that value
                first_mm_above_threshold = df.at[first_idx_above_threshold, mm_column]

                print("First above threshold:", {float(first_val_above_threshold)}, 
                    ", idx = ", {int(first_idx_above_threshold)})

                return first_idx_above_threshold

            else:
                print(f"Starting kN value of {sheet} is at above the threshold.")
                return 0
        
        else:
            print("get_closest_to_threshold for normal dataframe. No function yet implemented")

    def get_start_end_idx_val(self):
        if isinstance(self.dataframe, dict):
            end_idx_all = self.__get_idx_req_mm()   
            
            for sheet, df in self.dataframe.items():
                start_idx = self.get_closest_to_threshold(sheet)  

                end_idx = start_idx + end_idx_all

                #DEBUG: print(f"For {sheet}: \n\tStart idx = {start_idx} \n\tend idx = {end_idx}\n \t{(end_idx-start_idx)} total range")
                
                self.idx_start_end_dict[sheet]['start_idx'] = start_idx
                self.idx_start_end_dict[sheet]['end_idx'] = end_idx

    def extract_data_from_df(self): 
        if isinstance(self.dataframe, dict):
            if self.idx_start_end_dict is None:
                self.get_start_end_idx_val()

            new_dict_df = {}
            for sheet, df in self.dataframe.items():
                start = self.idx_start_end_dict[sheet]['start_idx']
                end = self.idx_start_end_dict[sheet]['end_idx']

                columns_to_extract = df.columns[1:3].tolist() 
                extracted_data = df.loc[start:end, columns_to_extract]
                
                if start > 0:
                    first_mm_above_threshold = df.at[start,mm_column] # Using labels 
                    print(f"\nDEBUG: mm of start = {first_mm_above_threshold}")
                    extracted_data[mm_column] = extracted_data[mm_column] - first_mm_above_threshold
                
                new_dict_df[sheet] = extracted_data

            return new_dict_df
        else:
            print("Function for single dataframe not yet added")
            return None

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


# Import excel tools module as 'excel_mod'
sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas\Excel')
excel_mod = __import__('MODULE_excel_functions')

script_dir = os.path.dirname(os.path.abspath(__file__))

if INPUT_DATA_IN_SCRIPT_DIR == True:
    inputData_dir = os.path.join(script_dir, 'Input_folder') 
else:
    inputData_dir = r'C:\Users\Lolo\Desktop\Graph Patty\Semi-Raw' # Folder that would contain the excel files

main()