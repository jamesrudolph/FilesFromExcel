import pandas as pd
import json
import re

def excel_to_json(excel_file, column_name):
    # Read the Excel file
    df = pd.read_excel(excel_file)
    
    # Iterate over each cell in the specified column
    for cell in df[column_name]:
        # Create a JSON file for each cell

        match = re.search('{"id":"(.+?)","', cell)
        if match:
            file_name = match.group(1) + '.json'

            cell = json.loads(cell)

            with open("json/" + file_name, 'w') as file:
                json.dump(cell, file)
            print(f'{file_name} created successfully!')
        else:
            print(f'File creation failed: {cell}')
    
    print('JSON files created successfully!')

# Specify the Excel file path and column name
excel_file = './json.xlsx'
column_name = 'json'

# Call the function
excel_to_json(excel_file, column_name)

