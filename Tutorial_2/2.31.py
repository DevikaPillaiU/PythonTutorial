from collections import Counter

def rem_all_dup(lst):
    freq = Counter(lst)
    return [x for x in lst if freq[x] == 1]

n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

print(f"\nList after completely removing duplicates: {rem_all_dupl(numbers)}")
