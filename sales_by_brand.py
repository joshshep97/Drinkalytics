from openpyxl import Workbook
from extensions import df
import calendar

def get_sales_by_brand():
    sales_by_brand = df.groupby('Brand')['Sales Amount'].sum().sort_values(ascending=False)
    print('\nSales by Drink:')
    print(sales_by_brand)

    # Create a new workbook
    workbook = Workbook()

    # Select the active sheet
    sheet = workbook.active

    # Append the data
    sheet.append(['Drink Name', 'Drink Sales'])
    for brand_name, brand_sales in sales_by_brand.items():
        sheet.append([brand_name, brand_sales])

    # Save the workbook
    workbook.save(f'workbooks/aggregated/sales_by_brand{calendar.month_name.lower()}.xlsx')

    # Close the workbook
    workbook.close()