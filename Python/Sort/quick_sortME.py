def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[len(arr)// 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [20,3,4,1,7,8,9]
print(quick_sort(arr))