 def calculate_sums_and_averages(values):
    positive_sum = 0  
    negative_sum = 0  
    positive_count = 0  
    negative_count = 0

    for value in values:
        if value > 0:
            positive_sum += value
            positive_count += 1
        elif value < 0:
            negative_sum += value
            negative_count += 1

    positive_avg = positive_sum / positive_count if positive_count > 0 else 0
    negative_avg = negative_sum / negative_count if negative_count > 0 else 0

    return positive_sum, positive_avg, negative_sum, negative_avg


numbers = []
for i in range(4):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

positive_sum, positive_avg, negative_sum, negative_avg = calculate_sums_and_averages(numbers)

print(f"Sum of positive numbers: {positive_sum}")
print(f"Average of positive numbers: {positive_avg:.2f}")
print(f"Sum of negative numbers: {negative_sum}")
print(f"Average of negative numbers: {negative_avg:.2f}")
