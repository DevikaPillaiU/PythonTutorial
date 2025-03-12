def convert_to_hms(total_seconds):
    hrs = total_seconds // 3600
    mins = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    return f"{hrs:02}:{mins:02}:{secs:02}"

total_seconds = int(input("Enter the time in seconds: "))
formatted_time = convert_to_hms(total_seconds)
print("Time in HH:MM:SS format", formatted_time) 
