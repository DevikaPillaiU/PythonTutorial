def find_prime_factors(number):
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            print(divisor, end=" ")
            number //= divisor
        else:
            divisor += 1

input_number = int(input("Enter a number: "))
print("Prime factors:", end=" ")
find_prime_factors(input_number)
