def binary_search_iterative(arr, low, high, target):
    if high >= low:
        mid = (high+low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            return binary_search_iterative(arr, low, mid-1, target)
        else:
            return binary_search_iterative(arr, mid+1, high, target)
    else:
        return -1

def binary_search_recursive(arr, target):
    low = 0
    high = len(arr)-1
    while high>=low:
        mid = (low+high) // 2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return -1


arr = [1, 3, 5, 7, 9]
print(binary_search_iterative(arr, 0, len(arr)-1, 3))
print(binary_search_recursive(arr, 3))

