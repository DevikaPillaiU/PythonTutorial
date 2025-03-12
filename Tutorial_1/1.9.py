def check_prime(number):
    if number <= 1:
        return False 
    
    for divisor in range(2, int(number ** 0.5) + 1):  
        if number % divisor == 0:
            return False  
    
    return True  

num = int(input("Enter a number: "))

if check_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
