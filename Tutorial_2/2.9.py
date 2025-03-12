text = input("Enter the string: ")

length = len(text)
middle = length // 2

for i in range(middle - 1, -1, -1):
    print(text[i], end="")
for i in range(length - 1, middle - 1, -1):
    print(text[i], end="")
