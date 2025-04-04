import pandas as pd

dataset = pd.read_excel("output.xlsx", index_col=0)

print("Dataset read from output.xlsx:")
print(dataset)
