from openpyxl import Workbook
import pandas as pd
from extensions import df

def get_sales_by_drink():
    sales_by_drink = df.groupby('Drink Name')['Sales Amount'].sum().sort_values(ascending=False)
    print('\nSales by Drink:')
    print(sales_by_drink)

    # Create a new workbook
    workbook = Workbook()

    # Select the active sheet
    sheet = workbook.active

    # Append the data
    sheet.append(['Drink Name', 'Drink Sales'])
    for drink_name, drink_sales in sales_by_drink.items():
        sheet.append([drink_name, drink_sales])

    # Save the workbook
    workbook.save('workbooks/aggregated/sales_by_drink.xlsx')

    # Close the workbook
    workbook.close()