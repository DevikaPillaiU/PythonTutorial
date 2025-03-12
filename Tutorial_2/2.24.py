from collections import Counter

def calc_mode(values):
    freq_count = Counter(values)
    max_occurrence = max(freq_count.values())
    mode_values = [val for val, count in freq_count.items() if count == max_occurrence]
    return mode_values

num_elements = int(input("Enter the number of elements: "))
value_list = [int(input(f"Enter number {index+1}: ")) for index in range(num_elements)]

print(f"\nThe mode is: {calc_mode(value_list)}")
