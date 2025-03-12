num_elements = int(input("Enter the number of elements: "))

sum_even = 0

for index in range(num_elements):
    value = int(input(f"Enter number {index + 1}: "))
    if value % 2 == 0:
        sum_even += value

print(f"\nSum of all even numbers: {sum_even}")
