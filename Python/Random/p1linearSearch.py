# Define the array
array = [3, 5, 2, 9, 7, 1]
found = False

# Check if 7 is present in the array
for element in array:
    if element == 7:
        found = True
        break

# Print the result
if found:
    print("Yes")
else:
    print("No")