
def sumofc(limit):
    total = 0 

    for i in range(2, limit + 1, 2): 
        total += i ** 3 

    return total

num = int(input("Enter a positive integer: "))

if num <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Sum of cubes of even numbers up to {num}: {sumofc(num)}")
