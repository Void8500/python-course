# Input: total seconds
total_seconds = int(input("Enter time in seconds: "))

# Calculate hours 
hours = total_seconds // 3600             #3610//3600 -> 

# Remaining seconds after hours
remaining_seconds = total_seconds % 3600

# Calculate minutes
minutes = remaining_seconds // 60

# Remaining seconds after minutes
seconds = remaining_seconds % 60

# Output result
print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), and {seconds} second(s)")
