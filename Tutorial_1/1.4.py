def num_compare(n1, n2):
    if n1 > n2:
        print(f"{n1} is the largest")
        print(f"{n2} is the smallest")
    elif n1 == n2:
        print(f"{n1} & {n2} are equal")
    else:
        print(f"{n2} is the largest")
        print(f"{n1} is the smallest")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
num_compare(n1, n2)
