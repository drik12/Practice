# Function to perform Selection Sort on an array
def selection_sort(arr):
    n = len(arr)  # Determine the size of the array
    for i in range(n - 1):
        min_idx = i  # Assume the first unsorted element is the smallest
        # Find the minimum element in the unsorted portion of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update min_idx if a smaller element is found
        # Swap the found minimum element with the first unsorted element
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

# Main function equivalent
if __name__ == "__main__":
    # Initialize the array
    arr = [64, 25, 12, 22, 11]
    
    # Sort the array using Selection Sort
    selection_sort(arr)
    print("Sorted Array:" , arr)