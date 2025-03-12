for number in range(100, 1001):
    digit_sum = 0
    temp = number
    
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    if digit_sum % 9 == 0:
        print(number, end=" ")
