import pandas as pd

values = [[15, 25, 35], [45, 55, 65], [75, 85, 95]]

row_labels = ['X', 'Y', 'Z']
col_labels = ['Feature1', 'Feature2', 'Feature3']

data_frame = pd.DataFrame(values, index=row_labels, columns=col_labels)

print("Constructed DataFrame:")
print(data_frame)
