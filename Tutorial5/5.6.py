import pandas as pd

records = [
    [1, "Linus Torvalds", "Finland", "Linux Kernel", 1991],
    [2, "Tim Berners-Lee", "England", "World Wide Web", 1990],
    [3, "Guido van Rossum", "Netherlands", "Python", 1991]
]

headers = ["ID", "Full Name", "Nation", "Achievement", "Year"]

data_frame = pd.DataFrame(records, columns=headers)

def save_to_csv(data, filename):
    data.to_csv(filename, index=False)
    print(f"Data successfully written to {filename}!")

save_to_csv(data_frame, "contributors_data.csv")
