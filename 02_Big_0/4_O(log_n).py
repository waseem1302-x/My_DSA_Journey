""" 

    O(log n) mean?

    The work shrinks the problem size by half (or some factor) in each step.
    So instead of going through all elements (O(n)), you cut it down fast.
    If n = 16 → steps = 4 (because log₂16 = 4).
    If n = 1,000,000 → only ~20 steps



    Where does O(log n) happen?

    Binary Search (classic example).
    Balanced Binary Search Trees (BSTs).
    Divide & Conquer algorithms (like Merge Sort, Quick Sort).
    Heap operations (insert, delete).

"""

# Example: Binary Search


# The goal is to find the target 11 in the sorted array nums = [1, 3, 5, 7, 9, 11, 13].

""" 

Step 1: Initial Search
    Array: [1, 3, 5, 7, 9, 11, 13]
    left = 0, right = 6
    mid = (0 + 6) // 2 = 3, arr[mid] = 7
    Decision:
    arr[mid] < target → Update left = mid + 1 = 4

Step 2: Narrowed Search Space
    Array: [9, 11, 13] (only considering indices 4 to 6)
    left = 4, right = 6
    mid = (4 + 6) // 2 = 5, arr[mid] = 11
    Decision:
    arr[mid] == target → Target found at index 5

"""  

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2   
        if arr[mid] == target:
            return mid                     
        elif arr[mid] < target:
            left = mid + 1               
        else:
            right = mid - 1
    return -1

# Sorted array
nums = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(nums, 11))  # Output: 5

