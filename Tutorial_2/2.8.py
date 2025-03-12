s= input("Enter the string")
ss1= input("Enter the substring ")
ss2= input("Enter the new substring ")

if ss1 in s:
    s = s.replace(ss1,ss2)
    print(s)
