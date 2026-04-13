# Bubble Sort Program

n = int(input("Enter number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

# Bubble Sort
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            # swap
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("After pass", i + 1, ":", arr)

print("Sorted array:", arr)