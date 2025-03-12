def exp(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

base = int(input("Enter the base (X): "))
exponent = int(input("Enter the exponent (Y): "))

print(f"{base}^{exponent} = {exp(base, exponent)}")
