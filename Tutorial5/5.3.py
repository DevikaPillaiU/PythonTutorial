import pandas as pd

values = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

row_names = ['X', 'Y', 'Z']

data_table = pd.DataFrame(values, index=row_names, columns=[f'Column{i+1}' for i in range(len(values[0]))])

def export_dataframe_to_excel(dataframe, file_name):
    dataframe.to_excel(file_name, index=True)
    print(f"Data written to {file_name}")

export_dataframe_to_excel(data_table, "result.xlsx")
