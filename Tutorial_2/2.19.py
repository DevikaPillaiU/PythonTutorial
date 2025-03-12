def compute_fibonacci(position):
    if position <= 0:
        return "Invalid input. Please enter a positive integer."
    elif position == 1:
        return 0
    elif position == 2:
        return 1
    else:
        return compute_fibonacci(position - 1) + compute_fibonacci(position - 2)

user_input = int(input("Enter the position (n) to find the Fibonacci number: "))
print(f"The {user_input}th Fibonacci number is: {compute_fibonacci(user_input)}")
