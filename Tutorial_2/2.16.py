def is_even_or_odd(value):
    if value % 2 == 0:
        print(f"{value} is Even")
    else:
        print(f"{value} is Odd")

def number_sign(value):
    if value > 0:
        print(f"{value} is Positive")
    elif value < 0:
        print(f"{value} is Negative")
    else:
        print(f"{value} is Zero")

def find_factors(value):
    print(f"Factors of {value}: ", end="")
    for i in range(1, value + 1):
        if value % i == 0:
            print(i, end=" ")
    print()

while True:
    print("\nMenu:")
    print("1. Check Even or Odd")
    print("2. Check if Number is Positive, Negative, or Zero")
    print("3. Generate Factors of a Number")
    print("4. Exit")

    user_choice = int(input("Enter your choice (1-4): "))

    if user_choice == 1:
        user_input = int(input("Enter a number: "))
        is_even_or_odd(user_input)
    elif user_choice == 2:
        user_input = int(input("Enter a number: "))
        number_sign(user_input)
    elif user_choice == 3:
        user_input = int(input("Enter a number: "))
        find_factors(user_input)
    elif user_choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a valid option (1-4).")
