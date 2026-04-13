# Function to implement bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap arr[j] and arr[j + 1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Given array
arr = [6, 5, 3, 1, 8, 7, 2, 4]
# Sort the array using bubble sort
bubble_sort(arr)
# Print the sorted array elements separated by space
print( ' '.join(map(str, arr)))
