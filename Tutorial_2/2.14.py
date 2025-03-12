def compute_factorial(num):
    if num == 0 or num == 1:
        return 1
    fact_result = 1
    for i in range(2, num + 1):
        fact_result *= i
    return fact_result

def combination(n_val, r_val):
    if r_val > n_val:
        return "r cannot be greater than n"
    
    return compute_factorial(n_val) // (compute_factorial(r_val) * compute_factorial(n_val - r_val))

n_input = int(input("Enter value of n: "))
r_input = int(input("Enter value of r: "))

print(f"nCr ({n_input}C{r_input}) = {combination(n_input, r_input)}")
