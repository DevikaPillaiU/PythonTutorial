def sod(number):
    number = abs(number)
    total_sum = 0

    while number > 0:
        digit = number % 10
        total_sum += digit
        number //= 10

    return total_sum

num = int(input("Enter a number: "))

print(f"Sum of digits: {sod(num)}")
