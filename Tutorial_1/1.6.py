def rt_tri(s1, s2, s3):
    sides = sorted([s1, s2, s3])
    
    if round(sides[0]**2 + sides[1]**2, 5) == round(sides[2]**2, 5):
        return "Yes, it is a right-angled triangle."
    else:
        return "No, it is not a right-angled triangle."

s1 = float(input("Enter first side: "))
s2 = float(input("Enter second side: "))
s3 = float(input("Enter third side: "))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print(rt_tri(s1, s2, s3))
else:
    print("Invalid triangle. The sum of any two sides must be greater than the third side.")
