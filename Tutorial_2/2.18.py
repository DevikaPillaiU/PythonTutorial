def compute_factorial(val):
    if val == 0 or val == 1:
        return 1
    return val * compute_factorial(val - 1)

user_input = int(input("Enter a number: "))

if user_input < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {user_input} is {compute_factorial(user_input)}")
