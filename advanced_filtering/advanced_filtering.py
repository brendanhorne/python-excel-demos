import pandas as pd

table_data = pd.read_excel('table.xlsx', dtype="int")
condition_1 = (table_data['a'] == 1) & (table_data['b'] == 1)
condition_2 = (table_data['a'] == 2) & (table_data['c'] == 1)
condition_3 = (table_data['b'] == 1) & (table_data['d'] == 1)
condition_4 = (table_data['a'] == 1) & ((table_data['b'] != table_data['c']) & (table_data['b'] != table_data['c']))

filtered_data = table_data[condition_1 | condition_2 | condition_3 | condition_4]

filtered_data.to_excel('filtered_table.xlsx')