# create mock data for 8 fake restaurants
from get_mock_data import get_mock_data
from os import path

if path.exists('workbooks/aggregated/aggregated_data.xlsx'):
    print('Path already Exists')
else:
    get_mock_data()
    print('Path Created')

# aggregate the data in a single .xlsx file
from get_mock_data import aggregate_data
aggregate_data()

# get data by drink and type and export to .xlsx
from get_stats import get_stats
from sales_by_drink import get_sales_by_drink
from sales_by_type import get_sales_by_type
from sales_by_brand import get_sales_by_brand

if __name__ == '__main__':
    if path.exists('workbooks/aggregated/aggregated_data.xlsx'):
        print('Database exists')
        print(get_stats())
        print(get_sales_by_drink())
        print(get_sales_by_type())
        print(get_sales_by_brand())
    else:
        print('Database does not exist')

    