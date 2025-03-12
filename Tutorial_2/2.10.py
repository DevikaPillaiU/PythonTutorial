pwd = input("Enter the password: ")
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_chars = "$@#"

if len(pwd) >= 6:
    for ch in pwd:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Password is valid")
    else:
        print("Invalid password")

else:
    print("Invalid password")
