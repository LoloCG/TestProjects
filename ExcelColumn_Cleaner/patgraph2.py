# What the script is meant to do with the excel
    # get all sheet names of an excel
    # upload their data into the df_dict (dictionary data)
    # for each sheet, Obtain max kN and its mm
    # take the highest mm among them and add 1/3
    # obtain data from kN and mm columns from beginning to the index of mm+1/3
    # paste into a new spreadsheet

import pandas as pd
import os

kN_column = "Fuerza (kN)"
mm_column = "Carrera (mm)"

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, 'TestExcel.xlsx') 

excel_file = pd.ExcelFile(file_path)

sheet_names = excel_file.sheet_names
print("Sheet names:", sheet_names)

df_dict = pd.read_excel(file_path, sheet_name=sheet_names)

mm_values = []
max_mm_value = -float('inf')
max_mm_sheet = None

for sheet, df in df_dict.items():
    max_kN_value = df[kN_column].max()
    index_max_kN = df.index[df[kN_column] == max_kN_value][0]
    
    mm_of_kN = df.at[index_max_kN, mm_column]

    mm_values.append(mm_of_kN)

    if mm_of_kN > max_mm_value:
        max_mm_value = mm_of_kN
        max_mm_sheet = sheet
    
    print(str({sheet}), "max kN =", max_kN_value, ", index =", index_max_kN, ", mm =", mm_of_kN)

print("max mm = ", max_mm_value, " in ", max_mm_sheet)

df_max_mm = df_dict[max_mm_sheet]

req_mm_val = max_mm_value + (max_mm_value/3)

closest_req_mm = df_max_mm[mm_column].iloc[(df_max_mm[mm_column] - req_mm_val).abs().argsort()[0]]
idx_closest_req_mm = df_max_mm.index[df_max_mm[mm_column] == closest_req_mm][0]

print("req_mm_val =", req_mm_val, "closest = ", closest_req_mm, "at index:", idx_closest_req_mm)

df_clean = {}

for sheet, df in df_dict.items():
    print(f"Processing sheet: {sheet}")
    columns_to_extract = df.columns[1:3].tolist() # determines which columns to extract from the DataFrame.
    
    extracted_data = df.loc[0:idx_closest_req_mm, columns_to_extract] # extracts a portion of the DataFrame df based on specified columns and row indices.

    print("extracted data of ", {sheet})

    df_clean[sheet] = pd.DataFrame(extracted_data) # creates a new DataFrame from the extracted data and assigns it to the dictionary df_all using the sheet name as the key.

print("new excel created")
output_path = os.path.join(script_dir, 'NewExcel2.xlsx')

with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book

    for sheet_name, df in df_clean.items():
        print(f"Adding data from sheet: {sheet_name}")
        clean_sheet_name = f"{sheet_name}_new"
        df.to_excel(writer, sheet_name=clean_sheet_name, index=False)  
    
    df.to_excel(writer, sheet_name="Chart", index=False)
    worksheet = writer.sheets['Chart']

    print("Creating chart...")
    
    chart = workbook.add_chart({'type': 'line'})
    
    for sheet_name, df in df_clean.items():
        
        clean_sheet_name = f"{sheet_name}_new"
        last_row = len(df)
        
        print(f"Plotting data from {sheet_name} as:", clean_sheet_name)

        chart.add_series({
            'name':         f'{sheet_name} Data',
            'categories':   [f"{clean_sheet_name}", 1, 1, last_row, 1],
            'values':       [f"{clean_sheet_name}", 1, 0, last_row, 0],
            'marker':       {'type': 'none'},
            'line':         {'width': 2.5},
            'smooth':     True,
        })

    chart.set_x_axis({
        'name': 'Carrera (mm)', 
        'num_format': '0.00',  # Set number format to display 2 decimal places
        'position_axis': 'on_tick', # Positions the axis on the tick marks.
        'major_gridlines': {'visible': True},
        'min': 0,
        'mas': 3,
        'interval_unit': 50,
        'interval_tick': 100 
        })
        
    chart.set_y_axis({
        'name': 'Fuerza (kN)',
        'num_format': '0.0',
        'major_gridlines': {'visible': True},
        })
    
    chart.set_legend({'position': 'bottom'})
    chart.set_style(1)
    worksheet.insert_chart(1, 2, chart)

print("opening excel...")
os.startfile(output_path) # open the excel file
print("...")

if os.path.exists(output_path):
    user_input = input(f"Eliminate excel? (Y/N): ").strip().upper()
    if user_input == 'Y':
        os.remove(output_path)
        print(f"File has been removed.")
    else:
        print(f"File was not removed.")
else:
    print(f"File does not exist.")


def unused_code():
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