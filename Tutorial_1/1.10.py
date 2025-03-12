def even_sum(count):
    total = 0  
    
    for i in range(count):
        number = int(input(f"Enter number {i+1}: "))  
        if number % 2 == 0: 
            total += number  
    
    return total 

num_count = int(input("Enter how many numbers: "))

print(f"Sum of even numbers: {even_sum(num_count)}")
