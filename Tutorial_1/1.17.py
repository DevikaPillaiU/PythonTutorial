num = int(input("Enter the value of num: "))

for i in range(1, num + 1):
    print(f"\nMul Table of {i}:") 
    for j in range(1, 11):  
        print(f"{i} x {j} = {i * j}") 
