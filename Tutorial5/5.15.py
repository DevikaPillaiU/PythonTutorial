import os

def list_directory_items():
    directory_contents = os.listdir()

    print("Items in the Current Working Directory:")
    for entry in directory_contents:
        print(entry)

list_directory_items()
