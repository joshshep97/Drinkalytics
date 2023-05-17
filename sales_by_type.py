from openpyxl import Workbook
import pandas as pd
from extensions import df

def get_sales_by_type():
    sales_by_drink_type = df.groupby('Drink Type')['Sales Amount'].sum().sort_values(ascending=False)
    print('\nSales by Drink Type:')
    print(sales_by_drink_type)

    by_type_workbook = Workbook()

    
    sheet = by_type_workbook.active

    sheet.append(['Drink Type', 'Drink Sales'])

    for drink_type, drink_sales in sales_by_drink_type.items():
        sheet.append([drink_type, drink_sales])

    # Save the workbook
    by_type_workbook.save('workbooks/aggregated/mock_analysis_by_type.xlsx')
    # Close the workbook
    by_type_workbook.close()