def is_armstrong_number(number):
    original_number = number
    num_digits = 0
    total_sum = 0
    
    n = number
    while n > 0:
        n //= 10
        num_digits += 1

    n = original_number
    while n > 0:
        digit = n % 10
        total_sum += digit ** num_digits
        n //= 10

    return original_number == total_sum

number = int(input("Enter a number: "))

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is NOT an Armstrong number.")
