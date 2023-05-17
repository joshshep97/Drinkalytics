from extensions import df

def get_stats():
    from get_mock_data import get_mock_data
    from os import path

    if path.exists('workbooks/aggregated/aggregated_data.xlsx'):
        print('Path already Exists')
    else:
        get_mock_data()
        print('Path Created')
    # Perform analysis
    total_sales = df['Sales Amount'].sum()
    average_sales = df['Sales Amount'].mean()

    max_sales_row = df[df['Sales Amount'] == df['Sales Amount'].max()]
    max_sales = {
        'Product Name': max_sales_row['Drink Name'].values[0],
        'Product Sales': max_sales_row['Sales Amount'].values[0],
    }

    min_sales_row = df[df['Sales Amount'] == df['Sales Amount'].min()]
    min_sales = {
        'Product Name': min_sales_row['Drink Name'].values[0],
        'Product Sales': min_sales_row['Sales Amount'].values[0],
    }

    # Display stats
    print(f'Total Sales: {total_sales}')
    print(f'Average Sales: {average_sales}')
    print(f'Max Sales: {max_sales["Product Name"]} - {max_sales["Product Sales"]}')
    print(f'Min Sales: {min_sales["Product Name"]} - {min_sales["Product Sales"]}')




