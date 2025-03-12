import math

def compute_factorial(num):
    fact_result = 1
    for i in range(1, num + 1):
        fact_result *= i
    return fact_result

def sine_maclaurin_series(angle_rad, terms):
    sine_approx = 0
    
    for n in range(terms):
        term = ((-1) ** n) * (angle_rad ** (2 * n + 1)) / compute_factorial(2 * n + 1)
        sine_approx += term

    return sine_approx

angle_degrees = float(input("Enter the value of x in degrees: "))
num_terms = int(input("Enter the number of terms: "))

angle_radians = math.radians(angle_degrees)

result = sine_maclaurin_series(angle_radians, num_terms)

print(f"sin({angle_degrees}) ≈ {result}")

