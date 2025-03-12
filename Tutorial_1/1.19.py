total_numbers = int(input("Enter the number of elements: "))

count_even = 0
count_odd = 0

for _ in range(total_numbers):

    value = int(input("Enter a number: "))
    if value % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Even numbers: {count_even}")
print(f"Odd numbers: {count_odd}")
