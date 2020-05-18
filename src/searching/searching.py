import sys
sys.path.append("../iterative_sorting")
from iterative_sorting import bubble_sort

def linear_search(arr, target):
    # Your code here
    for i in range (0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    arr = bubble_sort(arr)
    high = len(arr)
    low = 0
    print(arr)
    # Your code here
    while low < high:
        mid = (high+low)//2
        print("mid", mid)
        arr[mid]
        if target == arr[mid]:
            print("target", mid)
            return mid
        elif target > arr[mid]:
            low = mid
            print("low", low)
            
            
        else:
            high = mid
            print("high", high)

    return -1  # not found

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
target = 0
print(binary_search(arr1, 0))