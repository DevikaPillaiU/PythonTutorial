def check_prime(num):
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True

def classify_prime_composite(values):
    prime_list = [x for x in values if check_prime(x)]
    composite_list = [x for x in values if x > 1 and not check_prime(x)]
    return prime_list, composite_list

num_elements = int(input("Enter the number of elements: "))
value_list = [int(input(f"Enter positive integer {index+1}: ")) for index in range(num_elements) if int(input(f"Enter positive integer {index+1}: ")) > 0]

primes, composites = classify_prime_composite(value_list)

print(f"\nPrime numbers: {primes}")
print(f"Composite numbers: {composites}")
