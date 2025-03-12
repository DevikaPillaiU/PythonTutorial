def data_types(elements):
    int_list = [x for x in elements if isinstance(x, int) and not isinstance(x, bool)]
    float_list = [x for x in elements if isinstance(x, float)]
    str_list = [x for x in elements if isinstance(x, str)]
    return int_list, float_list, str_list

num_elements = int(input("Enter the number of elements: "))
data_list = [eval(input(f"Enter element {index+1}: ")) for index in range(num_elements)]

integers, floats, strings = data_types(data_list)

print(f"\nIntegers: {integers}")
print(f"Floats: {floats}")
print(f"Strings: {strings}")
