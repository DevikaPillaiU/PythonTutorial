def reverse(n):
    rev_num = 0
    
    while n > 0:
        digit = n % 10 
        rev_num = rev_num * 10 + digit  
        n //= 10
    
    return rev_num

number = int(input("Enter a number: "))

if number < 0:
    print(f"Reversed number: -{reverse(abs(number))}")
else:
    print(f"Reversed number: {reverse(number)}")

