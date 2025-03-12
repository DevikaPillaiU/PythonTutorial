
def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            return False
    return True

for number in range(2, 1000):
    if check_prime(number):
        print(number, end=" ")
