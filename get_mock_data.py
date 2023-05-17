from openpyxl import Workbook
import random
from lists import restaurants, drinks
import pandas as pd
import glob
from os import path
from datetime import date

def get_mock_data():
    # generates fake sales data from 8 fake restaurants and a list of 25 drinks
    for restaurant in restaurants:
        restaurant_path = restaurant.lower().replace(' ', '_') + '_' + str(date.today())
        wb = Workbook()
        sheet = wb.active

        # Header row
        sheet.append(['Sales Amount', 'Drink Name','Drink Type', 'Brand', 'Drink Price'])

        # Generate mock sales data
        for _ in range(200):
            random_drink = random.choice(drinks)
            sales_amount = random.randint(100, 600)
            drink_name = random_drink['drink_name']
            drink_type = random_drink['drink_type']
            drink_brand = random_drink['brand']
            drink_price = random.randint(8, 14)
            sheet.append([sales_amount, drink_name, drink_type, drink_brand, drink_price])

        wb.save(f'workbooks/{restaurant_path}_mock_sales_data.xlsx')
        wb.close()

# aggregates all the data from the 8 restaurants into a single spreadsheet
def aggregate_data():
    # Define the path to the directory where your spreadsheets are located
    path = 'workbooks/'

    # Retrieve the file names of all spreadsheets ending with "mock_sales_data.xlsx"
    file_names = glob.glob(path + '/*mock_sales_data.xlsx')

    # Create an empty list to store the DataFrames
    dfs = []

    # Iterate over the file names, read each spreadsheet, and append it to the list
    for file in file_names:
        df = pd.read_excel(file)
        dfs.append(df)

    # Check if any files were found
    if not dfs:
        print("No files found. Please verify the directory path and file names.")
        exit()

    # Concatenate the DataFrames in the list to create the aggregated DataFrame
    aggregated_data = pd.concat(dfs, ignore_index=True)

    # Perform any required analysis or manipulations on the aggregated data

    # Export the aggregated data to a new .xlsx file
    aggregated_data.to_excel('workbooks/aggregated/aggregated_data.xlsx', index=False)


