#Function to perform Insertion Sort on an array
def insertion_sort(arr):
    n = len(arr)  # Get the size of the array
    for i in range(1, n):
        key = arr[i]  # Element to be inserted into the sorted part
        j = i - 1

        # Shift elements of the sorted part to the right to make space for the key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key in its correct position
        arr[j + 1] = key

# Main function equivalent
if __name__ == "__main__":
    # Initialize the array
    arr = [5, 2, 4, 6]

    # Sort the array using Insertion Sort
    insertion_sort(arr)
    print("Sorted array: ", arr)