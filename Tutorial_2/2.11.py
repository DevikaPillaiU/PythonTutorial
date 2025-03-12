def dec_to_bin(num):
    bin_str = ""
    
    if num == 0:
        return "0"
    
    while num > 0:
        bin_str = str(num % 2) + bin_str  
        num = num // 2 
        print(bin_str) 
    
    return bin_str


decimal_num = int(input("Enter a decimal number: "))

print(f"Binary representation: {dec_to_bin(decimal_num)}")
