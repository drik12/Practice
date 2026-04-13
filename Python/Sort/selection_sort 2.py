def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        print(f"\nPass {i+1}: Starting from index {i}")

        # Find the smallest element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"   New minimum found at index {min_index} → {arr[min_index]}")

        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"   Swapped index {i} with index {min_index}")
        print("   Array now:", arr)

    return arr

# Example usage
nums = [64, 25, 12, 22, 11]
print("\nFinal Sorted Array:", selection_sort(nums))