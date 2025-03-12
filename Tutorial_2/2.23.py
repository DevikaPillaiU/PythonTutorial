def calc_median(values):
    values.sort()  
    size = len(values)
    
    if size % 2 == 1:
        return values[size // 2]  
    else:
        mid1, mid2 = values[size // 2 - 1], values[size // 2]  
        return (mid1 + mid2) / 2  

num_elements = int(input("Enter the number of elements: "))

value_list = []
for index in range(num_elements):
    element = float(input(f"Enter number {index+1}: ")) 
    value_list.append(element)

median_value = calc_median(value_list)
print(f"\nThe median is: {median_value}")
