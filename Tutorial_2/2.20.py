num_names = int(input("Enter the number of names: "))

name_list = []
for index in range(num_names):
    entered_name = input(f"Enter name {index + 1}: ")
    name_list.append(entered_name)

name_list.sort()

print("\nNames in alphabetical order:")
for sorted_name in name_list:
    print(sorted_name)
