arr = [10, 14, 19, 23, 27, 31, 35]

def binary_search(arr):
    low = 0
    high = len(arr) - 1

    target = 31


    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1

    return -1

print(binary_search(arr))