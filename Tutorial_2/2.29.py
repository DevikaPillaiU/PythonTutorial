def set_ops(set1, set2):
    union_res = set1 | set2
    intersection_res = set1 & set2
    diff_res1 = set1 - set2
    diff_res2 = set2 - set1
    symmetric_diff_res = set1 ^ set2
    return union_res, intersection_res, diff_res1, diff_res2, symmetric_diff_res

set1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))

union_res, intersection_res, diff_res1, diff_res2, symmetric_diff_res = set_ops(set1, set2)

print(f"\nUnion: {union_res}")
print(f"Intersection: {intersection_res}")
print(f"Difference (Set1 - Set2): {diff_res1}")
print(f"Difference (Set2 - Set1): {diff_res2}")
print(f"Symmetric Difference: {symmetric_diff_res}")
