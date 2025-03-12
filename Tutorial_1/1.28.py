lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

odd_sum = 0

for num in range(lower, upper + 1):
    if num % 2 != 0:
        odd_sum += num

print(f"Sum of odd numbers between {lower} and {upper} is {odd_sum}")
